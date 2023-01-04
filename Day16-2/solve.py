import re

class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def __repr__(self) -> str:
        return f'Graph({self.nodes})'

class Node:
    def __init__(self, id, name, value, neighbors) -> None:
        self.id = id
        self.name = name
        self.value = value
        self.neighbors = list(neighbors)

    def __repr__(self) -> str:
        return f'Node({self.name}, {self.id}, {self.value}, {self.neighbors})'

def solve(lines):
    r = re.compile(r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
    graph = Graph()
    id = 1

    for line in lines:
        line = line.strip()
        if line:
            matches = r.match(line)
            groups = matches.groups()
            node = Node(id, groups[0], int(groups[1]), groups[2].split(', '))
            id *= 2
            Graph.add_node(graph, node)

    queue = []

    s = set()
    queue.append(
        ('AA', 'AA', 0, 26, 0)
    )
    s.add(('AA', 'AA', 0, 26, 0))

    ans = 0

    while queue:
        node_e1, node_e2, flow, time, score = queue.pop()
        node1 = graph.nodes[node_e1]
        node2 = graph.nodes[node_e2]

        if time <= 0:
            if score > ans:
                ans = score
                print(ans)
            continue
        
        should_take1 = (flow & node1.id) != node1.id and node1.value > 0
        should_take2 = (flow & node2.id) != node2.id and node2.value > 0 and node1.name != node2.name
        for take1 in set([False, should_take1]):
            for take2 in set([False, should_take2]):
                for neighbor1 in node1.neighbors:
                    for neighbor2 in node2.neighbors:
                        if take1:
                            if take2:
                                next = (neighbor1, neighbor2, flow | node1.id | node2.id, time - 2, score + (node1.value * (time - 1)) + (node2.value * (time - 1)))
                            else:
                                next = (node1.name, neighbor2, flow | node1.id, time - 1, score + (node1.value * (time - 1)))
                        else:
                            if take2:
                                next = (neighbor1, node2.name, flow | node2.id, time - 1, score + (node2.value * (time - 1)))
                            else:
                                next = (neighbor1, neighbor2, flow, time - 1, score)
                                
                        if next in s:
                            continue
                        s.add(next)
                        queue.append(
                            next
                        )

    print(ans)


def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()