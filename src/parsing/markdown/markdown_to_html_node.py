from src.nodes.textnode import TextType
from src.nodes.parentnode import ParentNode
from src.nodes.leafnode import LeafNode
from src.parsing.block.block_to_block_type import block_to_block_type
from src.parsing.block.split_markdown_in_blocks import split_markdown_in_blocks
from src.parsing.text.text_to_textnode import text_to_textnode

def markdown_to_html_node(document):
    list_of_children = []
    blocked_doc = split_markdown_in_blocks(document)
    for block in blocked_doc:
        list_of_children.append(resolve_block(block))
    return ParentNode("div", list_of_children)


def resolve_lists(block, block_type):
    if block_type == "ordered list":
        tag = "ol"
    elif block_type == "unordered list":
        tag = "ul"
    else:
        
        return None

    items = []
    for subblock in block.split('\n'):
        if tag == "ul":
            subblock = subblock[1:].strip()
        elif tag == "ol":
            subblock = subblock[subblock.index(".") + 1:].strip()
        item_content = resolve_block(subblock, is_child_of_list=True)
        items.append(ParentNode("li", item_content))
    return ParentNode(tag, items)


def resolve_heading(block, block_type):
    if not block_type == "heading":
        return None
    return LeafNode(f"h{block[1:].count("#")+1}", block[(block[1:].count("#")+1):].strip())
def resolve_multiline_single_leaf(block, block_type):

    if block_type == "quote block":
        lines = [line[2:] for line in block.split("\n") if line.startswith(">")]
        children = []
        for line in lines:
            if len(line) == 0:
                children.append(LeafNode(None, "<br>"))
            else:
                children.append(LeafNode(None, line))
        return ParentNode("blockquote", children)
    if block_type == "code":
        new_block = ""
        for line in block.split("\n"):
            new_block += line + "\n"
        return ParentNode("pre", [LeafNode("code", new_block[3:-4].strip())])
    return None
def resolve_paragraph(block, block_type, is_child_of_list):
    textnodes = text_to_textnode(block)
    leafnodes = convert_textnodes_to_leafnode(textnodes)

    if is_child_of_list:
        return leafnodes
    if not block_type == "paragraph":
        return None
    return ParentNode("p", leafnodes)

def resolve_block(block, is_child_of_list=False):
    block_type = block_to_block_type(block)
    if resolve_multiline_single_leaf(block, block_type):
        result = resolve_multiline_single_leaf(block, block_type)
        return result
    if resolve_lists(block, block_type):
        result = resolve_lists(block, block_type)
        return result
    if resolve_heading(block, block_type):
        result = resolve_heading(block, block_type)
        return result
    result = resolve_paragraph(block, block_type, is_child_of_list)
    return result
    
def convert_textnodes_to_leafnode(textnodes):
    leafnodes = []
    for node in textnodes:
        if node.text_type == TextType.TEXT:
            leafnodes.append(LeafNode(None, node.text))
        elif node.text_type == TextType.BOLD:
            leafnodes.append(LeafNode("b", node.text))
        elif node.text_type == TextType.ITALIC:
            leafnodes.append(LeafNode("i", node.text))
        elif node.text_type == TextType.CODE:
            leafnodes.append(LeafNode("code", node.text))
        elif node.text_type == TextType.IMAGE:
            leafnodes.append(LeafNode("img", "", {"src":node.url, "alt":node.text}))
        elif node.text_type == TextType.LINK:
            leafnodes.append(LeafNode("a", node.text, {"href": node.url}))
    return leafnodes