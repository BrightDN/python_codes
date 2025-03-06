def split_markdown_in_blocks(text: str) -> list:
    blocks = []
    for block in text.split("\n\n"):
        if not block.strip():
            continue
        blocks.append("\n".join(line.strip() for line in block.split("\n") if line.strip()))
    return blocks