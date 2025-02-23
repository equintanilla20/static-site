import unittest

from textnode import TextNode, TextType
# from tqdm import tqdm


class TestTextNode(unittest.TestCase):
    # def test_all(self):
    #     tests = [
    #         self.test_eq,
    #         self.test_eq_02,
    #         self.test_repr_01,
    #         self.test_repr_02
    #     ]
        
    #     for test in tqdm(tests, desc='Running tests', unit='test'):
    #         test()
    
    
    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)
        
    
    def test_eq_02(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    
    def test_eq_03(self):
        node = TextNode('This is a text node', TextType.CODE, 'https://boot.dev')
        node2 = TextNode('This is a text node', TextType.CODE, 'https://boot.dev')
        self.assertEqual(node, node2)
    
    
    def test_repr_01(self):
        node = TextNode('This is a text node', TextType.TEXT)
        node2 = 'TextNode(This is a text node, TextType.TEXT, None)'
        self.assertEqual(str(node), node2)
    
    
    def test_repr_02(self):
        node = TextNode('This is a text node', TextType.ITALIC, 'https://boot.dev')
        node2 = 'TextNode(This is another text node, TextType.ITALIC, https://boot.dev)'
        self.assertNotEqual(str(node), node2)
    
    
    def test_text_node_to_html_node_01(self):
        node = TextNode('This is a text node', TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(str(html_node), 'LeafNode(b, This is a text node, None)')
    
    
    def test_text_node_to_html_node_02(self):
        node = TextNode('This is a text node', TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(str(html_node), 'LeafNode(i, This is a text node, None)')


    def test_text_node_to_html_node_03(self):
        node1 = TextNode('This is a text node', TextType.CODE)
        html_node1 = node1.text_node_to_html_node()
        node2 = TextNode('This is a text node', TextType.LINK, 'https://boot.dev')
        html_node2 = node2.text_node_to_html_node()
        self.assertNotEqual(str(html_node1), str(html_node2))


if __name__ == '__main__':
    unittest.main()
    