import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq_1(self):
        node1 = LeafNode('p', 'This is a paragraph node')
        node2 = LeafNode('p', 'This is a paragraph node')
        self.assertEqual(node1, node2)
    
    def test_eq_2(self):
        props1 = {'href': 'https://boot.dev'}
        props2 = {'href': 'https://google.com'}
        node1 = LeafNode('a', 'Boot', props=props1)
        node2 = LeafNode('a', 'Google', props=props2)
        self.assertNotEqual(node1, node2)
    
    def test_repr_1(self):
        node1 = LeafNode('p', 'This is a paragraph node')
        node2 = 'LeafNode(p, This is a paragraph node, None)'
        self.assertEqual(str(node1), node2)

if __name__ == '__main__':
    unittest.main()
