import re
from src.textnode import TextNode, TextType
from src.markup_parsing import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not delimiter in ["*", "**", "`"]:
        raise Exception("invalid delimiter")
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        while delimiter in current_text:
            first_delim = current_text.find(delimiter)
            second_delim = current_text.find(delimiter, first_delim + len(delimiter))
            if second_delim == -1:
                raise Exception(f"Text contains an opening '{delimiter}' but no closing '{delimiter}'")
                
            before_text = current_text[:first_delim]
            delim_text = current_text[first_delim + len(delimiter):second_delim]
            current_text = current_text[second_delim + len(delimiter):]
            if before_text:
                new_nodes.append(TextNode(before_text.strip(), TextType.TEXT))
            new_nodes.append(TextNode(delim_text, text_type))
        if current_text:    
            new_nodes.append(TextNode(current_text.strip(), TextType.TEXT))
    return new_nodes

def split_nodes_images(nodes):
    if len(nodes) == 0:
        return []
    return loopOverNodes(nodes, TextType.IMAGE)

def split_nodes_links(nodes):
    if len(nodes) == 0:
        return []
    return loopOverNodes(nodes, TextType.LINK)

def loopOverNodes(old_nodes, text_type):
        new_nodes = []
        prefix = ""
        use_function = extract_markdown_links
        if text_type == TextType.IMAGE:
            prefix = "!"
            use_function = extract_markdown_images
        for node in old_nodes:
            if node.text_type == TextType.CODE:
                new_nodes.append(TextNode(node.text, TextType.CODE))
                continue
            if node.text_type == TextType.IMAGE:
                new_nodes.append(TextNode(node.text, TextType.IMAGE, node.url))
                continue
            if len(use_function(node.text)) == 0:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue
            remaining_text = node.text
            for text, link in use_function(node.text):
                split_pattern = f"(?<!`){prefix}\[{text}\]\({link}\)(?!.*`)"
                sections = re.split(split_pattern, remaining_text, 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                if text_type == TextType.IMAGE:
                    new_nodes.append(TextNode(text, TextType.IMAGE, link))
                if text_type == TextType.LINK:
                    new_nodes.append(TextNode(text, TextType.LINK, link))
                remaining_text = sections[1]
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        return new_nodes
