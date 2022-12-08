data = []
with open('input.in', 'r') as f:
    for line in f.readlines():
        data.append(line.strip())

class Node:
    def __init__(self, name, size, parent):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = []
    
    def add_child(self, node):
        for child in self.children:
            if node.name == child.name:
                return child
        self.children.append(node)
        return node

    def get_size(self):
        size = 0
        for child in self.children:
            if child.size is not None:
                size += child.size
            else:
                size += child.get_size()
        return size
    
    def sum(self):
        size = 0
        for child in self.children:
            size += child.sum()
            if child.get_size() <= 100_000:
                size += child.get_size()
        return size

    def find(self, required, smallest):
        for child in self.children:
            if required <= child.get_size() < smallest:
                smallest = child.find(required, child.get_size())
        return smallest

    def __repr__(self):
        return self.children
    def __str__(self):
        return f'n: {self.name}, size: {self.size}, p: {self.parent}'


def solution():
    root = Node('/', 0, None)
    curr = root
    for i, line in enumerate(data):
        line = line.split()
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '..':
                curr = curr.parent
            else:
                curr = curr.add_child(Node(line[2], None, curr))
        elif line[0] == '$' and line[1] == 'ls':
            for inner in data[i+1:]:
                inner = inner.split()
                if inner[0] == '$':
                    break
                first, second = inner
                if first == 'dir':
                    curr.add_child(Node(second, None, curr))
                else:
                    curr.add_child(Node(second, int(first), curr))
    
    print("P1: ", root.sum())
    
    # Part 2
    space = 70_000_000
    update_space = 30_000_000
    req = update_space - (space - root.get_size())

    root = root.children[0]

    print("P2: ",root.find(req, root.get_size()))


solution()