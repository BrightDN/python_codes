from src.htmlnode import HTMLNode
from src.leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, props, children)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Your tag must not be of None-type")
        if self.children is None:
            raise ValueError("You must have children!")
        if len(self.children) == 0:
            return f"<{self.tag}></{self.tag}>"
        
        return f"<{self.tag}>" + "".join(map(lambda x: x.to_html(), self.children)) + f"</{self.tag}>"
