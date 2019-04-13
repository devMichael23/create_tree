from BinarySearchTree import BinarySearchTree, Node
from BracketTreeMaxLevel import BracketTreeMaxLevel

def getCountNodesInLevel(node:Node, level):
    if not Node:
        return 0
    if level == 0:
        return 1
    return getCountNodesInLevel(node.getLeftNode(), level-1) + getCountNodesInLevel(node.getRightNode(), level-1)

tree = BinarySearchTree()
lst = [6, 2, 1, 4, 3, 5, 8, 7, 9]
for i in range(len(lst)):
    tree[i] = lst[i]

print("3-е задание:")
print(tree)
print(getCountNodesInLevel(tree.getRoot(), 2))
print("\n")