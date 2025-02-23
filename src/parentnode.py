from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError('ParentNode tag cannot be None')
        if children is None:
            raise ValueError('ParentNode children cannot be None')
        
        super().__init__(tag, None, children, props)
    
    
    def to_html(self):
        child_nodes = ''
        for child in self.children:
            child_nodes += child.to_html()
        if self.props:
            return f'<{self.tag} {self.props_to_html()}>{child_nodes}</{self.tag}>'
        return f'<{self.tag}>{child_nodes}</{self.tag}>'
    
    
    def __eq__(self, obj):
        if not isinstance(obj, ParentNode):
            return False
        return self.tag == obj.tag and self.children == obj.children and self.props == obj.props
    
    
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'
    