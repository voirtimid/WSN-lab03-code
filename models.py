from typing import List


class Node:
    x: int
    y: int
    is_anchor: bool = False
    weight: int = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointX: {self.x}\tPointY: {self.y}\tAnchor: {self.is_anchor}\tWeight: {self.weight}"

    def __repr__(self):
        return str(self)


class Area:
    nodes: List[Node]

    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

