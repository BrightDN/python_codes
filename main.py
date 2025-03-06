import os
import shutil
import sys
from src.file_operations.move_from_static_to_public import move_from_static_to_public
from src.file_operations.generate_page import generate_page
from src.file_operations.generate_pages import generate_pages

def main(basepath = "/"):
    sys.argv

    if os.path.exists("public"):
        shutil.rmtree("public")
    
    os.mkdir("public")

    if os.path.exists("static"):
        move_from_static_to_public("static", "public")
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages("content", "template.html", "public", basepath)

if __name__ == "__main__":
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    main(basepath)