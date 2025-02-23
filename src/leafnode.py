from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError('LeafNode value cannot be None')
        super().__init__(tag, value, None, props)
    
    
    def to_html(self):
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
    
    
    def __eq__(self, obj):
        if not isinstance(obj, LeafNode):
            return False
        return self.tag == obj.tag and self.value == obj.value and self.props == obj.props
    
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    