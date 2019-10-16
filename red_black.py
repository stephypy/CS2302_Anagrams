class Node:
    def __init__(self, key, color='red'):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color


class RBTree:
    def __init__(self):
        self.root = Node(None, 'black')

    def insert(self, root, key):
        if root is None:
            return

    def inorder(self, node):
        if node is None:
            return
        if node.left:
            self.inorder(node.left)
        print(node.key)
        if node.right:
            self.inorder(node.right)
