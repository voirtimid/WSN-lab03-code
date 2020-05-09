import random


def generate_nodes():
    for i in range(50, 1001, 50):
        nodes = []
        with open(f"nodes/nodes_{i}.csv", "w") as f:
            while len(nodes) < 1000:
                random_x = random.randint(0, i)
                random_y = random.randint(0, i)
                if not nodes.__contains__((random_x, random_y)):
                    f.write(f"{random_x},{random_y}\n")
                    nodes.append((random_x, random_y))


def generate_random_topologies(size):
    for i in range(size):
        nodes = []
        with open(f"topologies/topology_{i}.csv", "w") as f:
            while len(nodes) < 1000:
                random_x = random.randint(0, 100)
                random_y = random.randint(0, 100)
                if not nodes.__contains__((random_x, random_y)):
                    f.write(f"{random_x},{random_y}\n")
                    nodes.append((random_x, random_y))


# generate_random_topologies(15)
