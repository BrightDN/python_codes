import re
def block_to_block_type(block):
    if block.startswith("#") and block.lstrip("#").startswith(" ") and block[1:].count("#") <= 5:
        return "heading"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    if resolve_ordered_list(block):
        return "ordered list"
    if resolve_multiline_code_block(block, r"^[*|-] ", "unordered list"):
        return "unordered list"
    if resolve_multiline_code_block(block, r"^\> ", "quote block"):
        return "quote block"
    return "paragraph"
    
def resolve_multiline_code_block(block, regex, block_type):
    lines = block.splitlines()
    for line in lines:
        if not re.match(regex, line):
            return None
    return block_type

def resolve_ordered_list(block):
    lines = block.splitlines()
    expected_number = 1
    for line in lines:
        match = re.match(r"^(\d+)\. ", line)
        if not match:
            return None
        number = int(match.group(1))
        if number != expected_number:
            return None
        expected_number += 1
    return "ordered list"