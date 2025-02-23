import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node1 = HTMLNode('p', 'This is a paragraph node')
        node2 = HTMLNode('p', 'This is a paragraph node')
        self.assertEqual(node1, node2)
    
    def test_eq_2(self):
        props1 = {'href': 'https://boot.dev'}
        props2 = {'href': 'https://google.com'}
        node1 = HTMLNode('a', 'Boot', props=props1)
        node2 = HTMLNode('a', 'Google', props=props2)
        self.assertNotEqual(node1, node2)
    
    def test_repr_1(self):
        node1 = HTMLNode('p', 'This is a paragraph node')
        node2 = 'HTMLNode(p, This is a paragraph node, None, None)'
        self.assertEqual(str(node1), node2)
    
if __name__ == '__main__':
    unittest.main()
