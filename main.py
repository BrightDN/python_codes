# import os
# import shutil
# from src.file_operations.move_from_static_to_public import move_from_static_to_public
# from src.parsing.markdown.markdown_to_html_node import markdown_to_html_node

# def extract_title(markdown: str) -> str | Exception:
#     """Expects a markdown file as input and returns the title (block that starts with "# ")
#     Raises an exception if there is no title present in the markdown input
#     """
#     from src.parsing.block.split_markdown_in_blocks import split_markdown_in_blocks
#     for block in split_markdown_in_blocks(markdown):
#         if block.startswith("# "):
#             return block[2:].strip()
#     raise Exception("There is no title in your markdown document, please ensure there is a title present")

# def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
#     """ This function takes in 3 parameters and moves all content from the from_path parameter into the designated places in the template_path parameter. Then it places the final result in the dest_path parameter
#     """
#     with open(from_path, 'r') as content, open(template_path, 'r') as temp, open(dest_path, "w") as dest:
#         content_file = content.read()
#         template_file = temp.read()
#         template_file.replace("{{ Title }}", extract_title(content_file))
#         html_content: str = markdown_to_html_node(content_file).to_html()
#         template_file.replace("{{ Content }}", html_content)

#         dest_path.write(html_content)


    
# def main():
#     if os.path.exists("public"):
#         shutil.rmtree("public")
#     os.mkdir("public")

#     if os.path.exists("static"):
#         move_from_static_to_public("static", "public")

#     generate_page("content/index.md", "template.html", "public/index.html")
# main()

import os
import shutil
from src.file_operations.move_from_static_to_public import move_from_static_to_public
from src.parsing.markdown.markdown_to_html_node import markdown_to_html_node

def extract_title(markdown: str) -> str | Exception:
    """Expects a markdown file as input and returns the title (block that starts with "# ")
    Raises an exception if there is no title present in the markdown input
    """
    from src.parsing.block.split_markdown_in_blocks import split_markdown_in_blocks
    for block in split_markdown_in_blocks(markdown):
        if block.startswith("# "):
            return block[2:].strip()
    raise Exception("There is no title in your markdown document, please ensure there is a title present")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    """ This function takes in 3 parameters and moves all content from the from_path parameter into the designated places in the template_path parameter. Then it places the final result in the dest_path parameter
    """
    with open(from_path, 'r') as content, open(template_path, 'r') as temp, open(dest_path, "w") as dest:
        content_file = content.read()

        template_file = temp.read()

        template_file = template_file.replace("{{ Title }}", extract_title(content_file))

        html_content: str = markdown_to_html_node(content_file).to_html()
        template_file = template_file.replace("{{ Content }}", html_content)

        dest.write(template_file)

def main():

    if os.path.exists("public"):
        shutil.rmtree("public")
    
    os.mkdir("public")

    if os.path.exists("static"):
        move_from_static_to_public("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()