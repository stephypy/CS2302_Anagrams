class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right

    def node_height(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            return 1 + self.node_height(node.right)
        if self.right is None:
            return 1 + self.node_height(node.left)
        return 1 + max(self.node_height(node.left), self.node_height(node.right))


class AVL:
    def __init__(self):
        self.root = None
        self.height = 0

    def update_height(self):
        self.height = self.root.node_height(self.root)

    def insert(self, key):
        self.root = self.inserting(self.root, key)
        self.update_height()

    def inserting(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self.inserting(root.left, key)
        else:
            root.right = self.inserting(root.right, key)

        self.update_height()
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key <= root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        y = z.right
        T1 = y.left
        y.left = z
        z.right = T1
        return y

    def right_rotate(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2
        return y

    def get_balance(self, root):
        if root is None:
            return 0
        return root.node_height(root.left) - root.node_height(root.right)

    def inorder(self, root):
        if root is None:
            return
        if root.left:
            self.inorder(root.left)
        print(root.key)
        if root.right:
            self.inorder(root.right)
