from BinarySearchTree import BinarySearchTree, Node

def getCountNodesInLevel(node:Node, level):
    if not Node:
        return 0
    if level == 0:
        return 1
    return getCountNodesInLevel(node.getLeftNode(), level-1) + getCountNodesInLevel(node.getRightNode(), level-1)