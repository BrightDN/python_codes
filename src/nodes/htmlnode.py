class HTMLNode:
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props= props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        string_to_return = " "
        for key, value in self.props.items():
            string_to_return += f"{key}=\"{value}\""
        return string_to_return
    
    def text_node_to_html_node(text_node):
        from src.nodes.leafnode import LeafNode
        from src.nodes.textnode import TextType
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                if text_node.url is None:
                    raise Exception("URL can not be absent")
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                if text_node.url is None:
                    raise Exception("URL can not be absent")
                return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
            case _:
                raise Exception("This type does not exist!")
            
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag 
            and self.value == other.value 
            and self.children == other.children 
            and self.props == other.props
        )