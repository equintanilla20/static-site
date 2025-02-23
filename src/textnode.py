from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'
    

class TextNode:
    
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
        
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode('span', self.text)
        elif self.text_type == TextType.BOLD:
            return LeafNode('b', self.text)
        elif self.text_type == TextType.ITALIC:
            return LeafNode('i', self.text)
        elif self.text_type == TextType.CODE:
            return LeafNode('code', self.text)
        elif self.text_type == TextType.LINK:
            return LeafNode('a', self.text, {'href': self.url})
        elif self.text_type == TextType.IMAGE:
            return LeafNode('img', '', {'src': self.url, 'alt': self.text})
        else:
            raise ValueError(f'Unknown text type: {self.text_type}')
    
    
    def __eq__(self, obj):
        if not isinstance(obj, TextNode):
            return False
        return self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url
    
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
