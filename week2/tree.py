from fractions import Fraction


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, value, traverse='pre'):
        self.__root = Node(value)
        self.traverse = traverse

    def insert(self, value):
        self.__insert(self.__root, value)

    def __insert(self, root, value):
        if root:
            if value > root.value:
                if not root.right:
                    root.right = Node(value)
                else:
                    self.__insert(root.right, value)
            else:
                if not root.left:
                    root.left = Node(value)
                else:
                    self.__insert(root.left, value)
        else:
            self.root = Node(value)

    def __iter__(self):
        if self.traverse == 'pre':
            self.__gen = self.__preorder(self.__root)
        elif self.traverse == 'in':
            self.__gen = self.__inorder(self.__root)
        elif self.traverse == 'post':
            self.__gen = self.__postorder(self.__root)
        return self

    def __preorder(self, root):
        if root:
            yield root
            yield from self.__preorder(root.left)
            yield from self.__preorder(root.right)

    def __inorder(self, root):
        if root:
            yield from self.__inorder(root.left)
            yield root
            yield from self.__inorder(root.right)

    def __postorder(self, root):
        if root:
            yield from self.__postorder(root.left)
            yield from self.__postorder(root.right)
            yield root

    def __next__(self):
        node = next(self.__gen)
        if node:
            return node
        raise StopIteration

    def __search(self, root, value):
        if root:
            if root.value > value:
                return self.__search(root.left, value)
            elif root.value < value:
                return self.__search(root.right, value)
            elif root.value == value:
                return root
        raise KeyError

    def search(self, value):
        return self.__search(self.__root, value)


def main():
    t = Tree('F')
    t.insert('B')
    t.insert('G')
    t.insert('A')
    t.insert('D')
    t.insert('C')
    t.insert('E')
    t.insert('I')
    t.insert('H')
    print(t.search('C'))
    it = iter(t)
    for i in it:
        print(i.value, end=' ')
    print()
    t.traverse = 'in'
    it = iter(t)
    for i in it:
        print(i.value, end=' ')
    print()
    t.traverse = 'post'
    it = iter(t)
    for i in it:
        print(i.value, end=' ')
    print()


if __name__ == '__main__':
    main()
