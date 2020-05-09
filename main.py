from trilateration_methods import *


def roundup(value):
    return int(math.ceil(value / 50.0)) * 50


# N: int = int(input("Enter the number of nodes:\t"))
# L: int = int(input("Enter the length of the field:\t"))
# R: float = int(input("Enter the radio depth:\t"))
# r: float = int(input("Enter signal noise:\t"))
# f: int = int(input("Enter percent of anchor nodes:\t"))

N: int = 150
L: int = 100
R: float = 30
r: float = 5
f: int = 20

num_anchor_nodes = math.ceil(N * f / 100)
noise = r

number_of_random_topologies = 15
sum_of_errors: float = 0
percent_of_found_nodes: float = 0

for j in range(number_of_random_topologies):

    file = open(f"topologies/topology_{j}.csv", "r")

    lines = file.readlines()

    area = models.Area()

    for i in range(N):
        x = int(lines[i].split(",")[0])
        y = int(lines[i].split(",")[1].replace("\n", ""))
        area.add_node(models.Node(x, y))

    for k in range(0, num_anchor_nodes):
        area.nodes[k].is_anchor = True

    anchor_nodes = area.nodes[0:num_anchor_nodes]
    nodes = area.nodes[num_anchor_nodes:]

    nodes_to_find = {}
    prediction_for_nodes = {}
    for node in nodes:
        hasAnchors, node_anchors = find_three_anchor_nodes(node, anchor_nodes, R)
        if hasAnchors:
            nodes_to_find[node] = node_anchors
            anchor_nodes_for_node = nodes_to_find[node]
            predicted_node = trilaterate(anchor_nodes_for_node[0][0], anchor_nodes_for_node[0][1][0],
                                         anchor_nodes_for_node[1][0], anchor_nodes_for_node[1][1][0],
                                         anchor_nodes_for_node[2][0], anchor_nodes_for_node[2][1][0],
                                         noise)
            # print(predicted_node)
            prediction_for_nodes[node] = predicted_node

            # This is only for iterative algorithm
            predicted_node.weight = node_anchors[0][0].weight + node_anchors[1][0].weight + node_anchors[2][0].weight + 1
            # anchor_nodes.append(predicted_node)

    error: float = 0
    for node in prediction_for_nodes:
        predicted_node = prediction_for_nodes[node]
        error += distance_between_two_nodes(node, predicted_node)
        # print(node)
        # print(predicted_node)

    # print(len(prediction_for_nodes))
    # print(len(nodes))
    # print(error)
    sum_of_errors += (error / (N - num_anchor_nodes))
    percent_of_found_nodes += (len(prediction_for_nodes) / len(nodes)) * 100

print(f"N = {N}\tL = {L}\tR = {R}\tr = {r}\tf = {f}")
print(f"Error: {round(sum_of_errors / number_of_random_topologies, 2)}")
print(f"Percent of found nodes: {round(percent_of_found_nodes / number_of_random_topologies, 2)}")

with open("results.txt", "a+") as result_file:
    result_file.write(f"N = {N}\tL = {L}\tR = {R}\tr = {r}\tf = {f}\n")
    result_file.write(f"Error: {round(sum_of_errors / number_of_random_topologies, 2)}\n")
    result_file.write(f"Percent of found nodes: {round(percent_of_found_nodes / number_of_random_topologies, 2)}\n")
