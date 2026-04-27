class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


    def to_html(self):
        raise NotImplementedError("Method Not Implemented")


    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html 


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have tag")
        elif self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        else:
            result = f"<{self.tag}>"
            for child in self.children:
                result += child.to_html()
            result += f"</{self.tag}>"
            return result

