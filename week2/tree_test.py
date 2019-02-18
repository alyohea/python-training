import unittest
from tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self):
        self.t = Tree('F')
        self.t.insert('B')
        self.t.insert('G')
        self.t.insert('A')
        self.t.insert('D')
        self.t.insert('C')
        self.t.insert('E')
        self.t.insert('I')
        self.t.insert('H')

    def test_insert(self):
        self.assertEqual('D', self.t._Tree__root.left.right.value)

    def test_search(self):
        self.assertEqual(self.t.search('C'), self.t._Tree__root.left.right.left)

    def test_preorder(self):
        nodes = [i.value for i in iter(self.t)]
        self.assertEqual(nodes, ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'])

    def test_inorder(self):
        self.t.traverse = 'in'
        nodes = [i.value for i in iter(self.t)]
        self.assertEqual(nodes, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

    def test_postorder(self):
        self.t.traverse = 'post'
        nodes = [i.value for i in iter(self.t)]
        self.assertEqual(nodes, ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'])


if __name__ == '__main__':
    unittest.main()
