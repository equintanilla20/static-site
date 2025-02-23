from enum import Enum
import re
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType


class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def text_to_textnodes(text):
    return (
        split_nodes_image(
            split_nodes_link(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter([TextNode(text, TextType.TEXT)], '`', TextType.TEXT), '**', TextType.TEXT), '*', TextType.TEXT))))


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    special_text_types = {
        '`': TextType.CODE,
        '**': TextType.BOLD,
        '*': TextType.ITALIC,
    }
    for node in old_nodes:
        if delimiter in node.text:
            split_text = node.text.split(delimiter)
            for i, text in enumerate(split_text):
                if i % 2 == 0:
                    if text:
                        nodes.append(TextNode(text, text_type))
                else:
                    nodes.append(TextNode(text, special_text_types[delimiter]))
        else:
            nodes.append(node)
    return nodes


def split_nodes_image(old_nodes):
    image_pattern = r"(!\[.*?\]\(.*?\))"
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = re.split(image_pattern, node.text)
            for part in parts:
                if part == '':
                    continue
                if part[0] != '!':
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    image = extract_markdown_images(part)
                    new_nodes.append(TextNode(image[0][0], TextType.IMAGE, image[0][1]))

    return new_nodes


def split_nodes_link(old_nodes):
    link_pattern = r"(?<!\!)(\[.*?\]\(.*?\))"
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = re.split(link_pattern, node.text)
            for part in parts:
                if part == '':
                    continue
                if part[0] != '[':
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    link = extract_markdown_links(part)
                    new_nodes.append(TextNode(link[0][0], TextType.LINK, link[0][1]))

    return new_nodes


def extract_markdown_images(text):
    nodes = []
    images = re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", text)
    for alt, src in images:
        nodes.append((alt, src))
    return nodes


def extract_markdown_links(text):
    nodes = []
    links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", text)
    for text, url in links:
        nodes.append((text, url))
    return nodes


def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split('\n\n'):
        if line != '' and line != '\n':
            blocks.append(line.strip())
    return blocks


def block_to_block_type(block):
    if block.startswith('#'):
        return BlockType.HEADING
    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    elif block.startswith('>'):
        return BlockType.QUOTE
    elif block.startswith('*') or block.startswith('-'):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == '.':
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            count = 0
            for char in block:
                if char == '#' and count < 6:
                    count += 1
                else:
                    break
                
            html_nodes.append(LeafNode(f'h{count}', block[2:]))
        elif block_type == BlockType.CODE:
            html_nodes.append(LeafNode('code', block[3:-3]))
        elif block_type == BlockType.QUOTE:
            html_nodes.append(LeafNode('blockquote', block[1:]))
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split('\n')
            html_node = HTMLNode('ul')
            for item in items:
                if html_node.children == None:
                    html_node.children = [LeafNode('li', item[2:])]
                else:
                    html_node.children.append(LeafNode('li', item[2:]))
            html_nodes.append(html_node)
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split('\n')
            html_node = HTMLNode('ol')
            for item in items:
                if html_node.children == None:
                    html_node.children = [LeafNode('li', item[3:])]
                else:
                    html_node.children.append(LeafNode('li', item[3:]))
            html_nodes.append(html_node)
        else:
            html_nodes.append(LeafNode('p', block))
    parent_node = HTMLNode('div', children=html_nodes)
    return parent_node


if __name__ == '__main__':

    node = TextNode(
        " and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        TextType.TEXT
    )
    node2 = TextNode(
        " and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        TextType.TEXT
    )
    node3 = TextNode(
        "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        TextType.TEXT
    )
    new_nodes = split_nodes_link([node])
    print(f'Links ::: {new_nodes}')
    new_nodes = split_nodes_image([node2])
    print(f'Images ::: {new_nodes}')
    new_nodes = text_to_textnodes(node3.text)
    print(f'All ::: {new_nodes}')
