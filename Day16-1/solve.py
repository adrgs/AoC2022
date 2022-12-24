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
        ('AA', 0, 30, 0)
    )
    s.add(('AA', 0, 30, 0))

    ans = 0

    while queue:
        node_name, flow, time, score = queue.pop()
        node = graph.nodes[node_name]

        if time <= 0:
            if score > ans:
                ans = score
            continue
        
        should_take = (flow & node.id) != node.id and node.value > 0
        for take in set([False, should_take]):
            for neighbor in node.neighbors:
                if take:
                    next = (neighbor, flow | node.id, time - 2, score + (node.value * (time - 1)))
                    if next in s:
                        continue
                    s.add(next)
                    queue.append(
                        next
                    )
                else:
                    next = (neighbor, flow, time - 1, score)
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