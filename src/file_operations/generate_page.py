from src.file_operations.extract_title import extract_title
from src.parsing.markdown.markdown_to_html_node import markdown_to_html_node

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