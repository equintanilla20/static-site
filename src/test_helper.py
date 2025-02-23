import unittest
from helper import *
from textnode import TextNode, TextType


class TestHelper(unittest.TestCase):
    
    def test_eq_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)


    def test_extract_images_01(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0][0], 'rick roll')
    
    
    def test_extract_links_01(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0][0], 'to boot dev')


    def test_split_nodes_image_01(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, 'This is text with a ')
        

    def test_split_nodes_link_01(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, 'This is text with a link ')


    def test_text_to_textnodes_01(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(len(new_nodes), 10)
        self.assertEqual(new_nodes[0].text, 'This is ')
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        
        
    def test_markdown_to_blocks_01(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)


    def test_block_to_block_type_01(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    
    def test_block_to_block_type_02(self):
        block = "```python\nprint('Hello, World!')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
        
    
    def test_markdown_to_html_node_01(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        html_node = markdown_to_html_node(markdown)

        self.assertEqual(len(html_node.children), 3)
        self.assertEqual(html_node.children[0].tag, 'h1')


if __name__ == '__main__':
    unittest.main()
    