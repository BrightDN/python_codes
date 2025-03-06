import os
import shutil
from src.file_operations.move_from_static_to_public import move_from_static_to_public
from src.file_operations.generate_page import generate_page
from src.file_operations.generate_pages import generate_pages

def main():

    if os.path.exists("public"):
        shutil.rmtree("public")
    
    os.mkdir("public")

    if os.path.exists("static"):
        move_from_static_to_public("static", "public")
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages("content", "template.html", "public")

if __name__ == "__main__":
    main()