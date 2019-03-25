import networkx as nx

class Node:
    def __init__(self, key, data, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return self.data

    def __iter__(self):
        if self:
            if self.hasLeftNode():
                for elem in self.left:
                    yield elem
            yield self.data
            if self.hasRightNode():
                for elem in self.right:
                    yield elem

    def hasLeftNode(self)->bool:
        return self.left

    def hasRightNode(self)->bool:
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChild(self):
        return self.right or self.left

    def hasBothChild(self):
        return self.right and self.left

    def replaceNodeData(self, key, data, left, right):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        if self.hasLeftNode():
            self.left.parent = self
        if self.hasRightNode():
            self.right.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def getlength(self):
        return self.size

    def __len__(self):
        return self.size

    def __setitem__(self,key, data):
       self.set(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        current = self.root
        if current:
            if current.hasLeftNode():
                for elem in current.left:
                    yield elem
            yield current.data
            if current.hasRightNode():
                for elem in current.right:
                    yield elem

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
       self.delete(key)

    def __str__(self):
        current = self.root
        while current:
            print(' '.join(str(node) for node in current))
            nextLevel = list()
            for n in current:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
                current = nextLevel

    def set(self,key, data):
        if self.root:
            self._set(key, data, self.root)
        else:
            self.root = Node(key, data)
        self.size += 1

    def _set(self,key, data, current):
        if data < current.data:
            if current.hasLeftNode():
                self._set(key, data, current.left)
            else:
                current.left = Node(key, data, parent=current)
        else:
            if current.hasRightNode():
                self._set(key, data, current.right)
            else:
                current.right = Node(key, data, parent=current)

    def get(self,key):
        if self.root:
            current = self._get(key, self.root)
            if current:
                return current.data
            else:
                return None
        else:
           return None

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def delete(self, key):
        if self.size > 1:
            current = self._get(key, self.root)
            if current:
                self.remove(current)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def getRoot(self):
        return self.root

    def spliceOut(self):
        current = None
        if current.isLeaf():
            if current.isLeftChild():
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.hasAnyChild():
            if current.hasLeftNode():
                if current.isLeftChild():
                    current.parent.left = current.left
                else:
                    current.parent.right = current.left
                current.left.parent = current.parent
            else:
                if current.isLeftChild():
                    current.parent.left = current.right
                else:
                    current.parent.right = current.right
                current.right.parent = current.parent

    def findSuccessor(self):
        current = None
        if current.hasRightNode():
            current = current.right.findMin()
        else:
            if current.parent:
                if current.isLeftChild():
                    current = current.parent
                else:
                    current.parent.right = None
                    current = current.parent.findSuccessor()
                    current.parent.right = self
        return current

    def findMin(self):
        current = None
        while current.hasLeftNode():
            current = current.left
        return current

    def remove(self, current):
        if current.isLeaf():
            if current == current.parent.left:
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.hasBothChild():
            current = current.findSuccessor()
            current.spliceOut()
            current.key = current.key
            current.data = current.data

        else:
            if current.hasLeftNode():
                if current.isLeftChild():
                    current.left.parent = current.parent
                    current.parent.left = current.left
                elif current.isRightChild():
                    current.left.parent = current.parent
                    current.parent.right = current.left
                else:
                    current.replaceNodeData(current.left.key, current.left.data, current.left.left, current.left.right)
            else:
                if current.isLeftChild():
                    current.right.parent = current.parent
                    current.parent.left = current.right
                elif current.isRightChild():
                    current.right.parent = current.parent
                    current.parent.right = current.right
                else:
                    current.replaceNodeData(current.right.key, current.right.data, current.right.left, current.right.right)

    def bracketPrint(self, current):
        if not current:
            return ''
        if (not current.hasLeftNode()) and (not current.hasRightNode()):
            return str(current.data)
        if not current.hasRightNode():
            return str(current.data) + "(" + self.bracketPrint(current.left) + ")"
        if not current.hasLeftNode():
            return str(current.data) + "(" + self.bracketPrint(current.right) + ")"
        return str(current.data) + "(" + self.bracketPrint(current.left) + ")" + "(" + self.bracketPrint(current.right) + ")"

tree = BinarySearchTree()
with open("tree.txt", "r") as file:
    lenght = int(file.readline())
    for i in range(lenght):
        data = int(file.readline())
        tree[i] = data

def printTree(tree:BinarySearchTree):
    for i in tree:
        print(i)

printTree(tree)
print()
print(tree.bracketPrint(tree.getRoot()))