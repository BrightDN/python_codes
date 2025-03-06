def extract_title(markdown: str) -> str | Exception:
    """Expects a markdown file as input and returns the title (block that starts with "# ")
    Raises an exception if there is no title present in the markdown input
    """
    from src.parsing.block.split_markdown_in_blocks import split_markdown_in_blocks
    for block in split_markdown_in_blocks(markdown):
        if block.startswith("# "):
            return block[2:].strip()
    raise Exception("There is no title in your markdown document, please ensure there is a title present")