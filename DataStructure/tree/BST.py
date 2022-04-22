class Node(object):
    __slots__ = "item", "left", "right", "height"

    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        self.height = 0


class BSTree(object):
    def __init__(self, root=None):
        self.root = root

    def get(self, key):
        return self.__get(self.root, key)

    def __get(self, node, key):
        if node is None:
            return None
        if key == node.item:
            return node.item
        if key < node.item:
            return self.__get(node.left, key)
        if key > node.item:
            return self.__get(node.right, key)

    def add(self, val):
        self.root = self.__add(self.root, val)

    def __add(self, node, val):
        if node is None:
            node = Node(val)
        if val == node.item:
            pass
        else:
            if val > node.item:
                node.right = self.__add(node.right, val)
            else:
                node.left = self.__add(node.left, val)
        return node

    def single_left_rotate(self,node):
        k1 = node.left
        node.left = k1.right

    def remove(self, key):
        return self.__remove(self.root, key)

    def __remove(self, node, key):
        if node is None:
            return None
        if key < node.item:
            node.left = self.__remove(node.left, key)
        if key > node.item:
            node.right = self.__remove(node.right, key)
        if key == node.item:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node.item = self.__get_max(node.left)
                node.left = self.__remove(node.left, node.item)
        return node

    def get_max(self):
        return self.__get_max(self.root)

    def __get_max(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def get_min(self):
        return self.__get_min(self.root)

    def __get_min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height


if __name__ == '__main__':
    bst = BSTree()
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 11, 14, 13, 21]
    for i in numbers:
        bst.add(i)
    print(bst)
    bst.remove(21)
    print(bst)
