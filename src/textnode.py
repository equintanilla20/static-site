from enum import Enum

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINKS = 'links'
    IMAGES = 'images'
    
class TextNode:
    
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    
    def __eq__(self, obj):
        if not isinstance(obj, TextNode):
            return False
        return self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url
    
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
