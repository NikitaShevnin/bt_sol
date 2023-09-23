class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self, key):
        self.key = key

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()

    def insert_left(self, new_node):
        self.left = new_node

    def insert_right(self, new_node):
        self.right = new_node

    def search(self, key):
        if self.key == key:
            return self

        if self.left is not None:
            temp = self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp = self.right.search(key)
            return temp
        return None

# реализация подсчета колличества элементов в дереве.
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def printTree(root, prev, isLeft):
    if root is None:
        return

    prev_str = '    '
    trunk = Trunk(prev, prev_str)
    printTree(root.right, trunk, True)

    if prev is None:
        trunk.str = '———'
    elif isLeft:
        trunk.str = '.———'
        prev_str = '   |'
    else:
        trunk.str = '`———'
        prev.str = prev_str

    showTrunks(trunk)
    print(' ' + str(root.data))
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    printTree(root.left, trunk, False)


if __name__ == '__main__':
    # Построить над деревом
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    # напечатать построенное бинарное дерево
    printTree(root, None, False)