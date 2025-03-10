class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError()
    
    
    def props_to_html(self):
        result = ''
        if self.props:
            for key, value in self.props.items():
                result += f'{key}="{value}" '
        return result.strip()
    
    
    def __eq__(self, obj):
        if not isinstance(obj, HTMLNode):
            return False
        return self.tag == obj.tag and self.value == obj.value and self.children == obj.children and self.props == obj.props
    
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    