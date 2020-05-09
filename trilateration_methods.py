import models
import math
import random


def trilaterate(p1: models.Node, d1: float, p2: models.Node, d2: float, p3: models.Node, d3: float, noise: float):
    i1 = p1.x
    i2 = p2.x
    i3 = p3.x

    j1 = p1.y
    j2 = p2.y
    j3 = p3.y

    d1 += random.randrange(-noise, noise) * d1 / 100
    d2 += random.randrange(-noise, noise) * d2 / 100
    d3 += random.randrange(-noise, noise) * d3 / 100

    if j1 == j2 and j2 != j3:
        i1, i3 = i3, i1
        j1, j3 = j3, j1

    predicted_x = (((2 * j3 - 2 * j2) * ((d1 * d1 - d2 * d2) + (i2 * i2 - i1 * i1) + (j2 * j2 - j1 * j1)) - (
            2 * j2 - 2 * j1) * ((d2 * d2 - d3 * d3) + (i3 * i3 - i2 * i2) + (j3 * j3 - j2 * j2))) / (
                           (2 * i2 - 2 * i3) * (2 * j2 - 2 * j1) - (2 * i1 - 2 * i2) * (2 * j3 - 2 * j2)))

    predicted_y = ((d1 * d1 - d2 * d2) + (i2 * i2 - i1 * i1) + (j2 * j2 - j1 * j1) + (
            predicted_x * (2 * i1 - 2 * i2))) / (2 * j2 - 2 * j1)

    return models.Node(predicted_x, predicted_y)


def distance_between_two_nodes(node1: models.Node, node2: models.Node):
    return math.sqrt(((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) * 1.0)


def is_collinear(p1, p2, p3):
    distance_p1_p2 = distance_between_two_nodes(p1, p2)
    distance_p1_p3 = distance_between_two_nodes(p1, p3)
    distance_p2_p3 = distance_between_two_nodes(p2, p3)
    if (distance_p1_p2 + distance_p2_p3 - distance_p1_p3 <= 0
            or distance_p2_p3 + distance_p1_p3 - distance_p1_p2 <= 0
            or distance_p1_p3 + distance_p1_p2 - distance_p2_p3 <= 0):
        return True
    else:
        return False


def find_three_anchor_nodes(node: models.Node, anchors, r):
    anchor_nodes = {}
    for anchor in anchors:
        distance = distance_between_two_nodes(node, anchor)
        if distance <= r:
            anchor_nodes[anchor] = distance, anchor.weight

    if len(anchor_nodes) < 3:
        return False, []
    else:
        sorted_anchors = sorted(anchor_nodes.items(), key=lambda item: item[1])

        # this is only for iterative algorithm 2
        # sorted_anchors = sorted(anchor_nodes.items(), key=lambda item: item[1][1])

        if is_collinear(sorted_anchors[0][0], sorted_anchors[1][0], sorted_anchors[2][0]):
            return False, []
        else:
            return True, sorted_anchors[:3]
