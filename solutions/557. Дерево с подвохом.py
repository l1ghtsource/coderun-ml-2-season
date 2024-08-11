class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, class_label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.class_label = class_label


def dfs(node, path, dataset):
    if node.class_label is not None:
        dataset.append(path[:])
        return

    path[node.feature - 1] = node.threshold - 1
    dfs(node.left, path, dataset)

    path[node.feature - 1] = node.threshold + 1
    dfs(node.right, path, dataset)


f, c, n = map(int, input().split())
lines = [input() for _ in range(2 * n)]

nodes = [None] * (len(lines) // 2 + 1)

for i in range(0, len(lines), 2):
    node_index = i // 2 + 1
    left, right = map(int, lines[i].split())
    if left == -1 and right == -1:
        class_label = int(lines[i + 1])
        nodes[node_index] = Node(class_label=class_label)
    else:
        feature, threshold = lines[i + 1].split()
        nodes[node_index] = Node(feature=int(feature), threshold=float(threshold))
        if left != -1:
            nodes[node_index].left = left
        if right != -1:
            nodes[node_index].right = right

for i in range(1, len(nodes)):
    if nodes[i].left:
        nodes[i].left = nodes[nodes[i].left]
    if nodes[i].right:
        nodes[i].right = nodes[nodes[i].right]

root = nodes[1]

dataset = []
path = [0] * f
dfs(root, path, dataset)

print(len(dataset))
for data in dataset:
    print(' '.join(f'{x:.1f}' for x in data))
