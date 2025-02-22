from src.textnode import TextType
from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.block_to_block_type import block_to_block_type
from src.split_markdown_in_blocks import split_markdown_in_blocks
from src.text_to_textnode import text_to_textnode

def markdown_to_html_node(document):
    list_of_children = []
    blocked_doc = split_markdown_in_blocks(document)
    for block in blocked_doc:
        list_of_children.append(resolve_block(block))
    return ParentNode("div", list_of_children)

def resolve_lists(block, block_type):
    if not block_type == "ordered list" and not block_type == "unordered list":
        return None
    list_type = "ul"
    list_of_leafnodes = []
    if(block_type == "ordered list"):
        list_type = "ol"
    for line in block.split("\n"):
        if list_type == "ul":
            line = line[2:]
        else:
            line = line[(line.find(". ")+2):]
        list_of_leafnodes.append(LeafNode("li", line))
    return ParentNode(list_type, list_of_leafnodes)
def resolve_heading(block, block_type):
    if not block_type == "heading":
        return None
    return LeafNode(f"h{block[1:].count("#")+1}", block[(block[1:].count("#")+1):].strip())
def resolve_multiline_single_leaf(block, block_type):

    if block_type == "quote block":
        lines = [line[2:] for line in block.split("\n")]
        new_block = "\n".join(lines)
        return LeafNode("blockquote", new_block)
    if block_type == "code":
        new_block = ""
        for line in block.split("\n"):
            new_block += line + "\n"
        return ParentNode("pre", [LeafNode("code", new_block[3:-4].strip())])
    return None
def resolve_paragraph(block, block_type):
    if not block_type == "paragraph":
        return None
    textnodes = text_to_textnode(block)
    leafnodes = convert_textnodes_to_leafnode(textnodes)
    return ParentNode("p", leafnodes)

def resolve_block(block):
    block_type = block_to_block_type(block)
    if resolve_multiline_single_leaf(block, block_type):
        return resolve_multiline_single_leaf(block, block_type)
    if resolve_lists(block, block_type):
        return resolve_lists(block, block_type)
    if resolve_heading(block, block_type):
        return resolve_heading(block, block_type)
    if resolve_paragraph(block, block_type):
        return resolve_paragraph(block, block_type)
    
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