import os
import shutil
import sys
from src.file_operations.move_from_static_to_public import move_from_static_to_public
from src.file_operations.generate_pages import generate_pages

def main(basepath = "/"):
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    
    os.mkdir("docs")

    if os.path.exists("static"):
        move_from_static_to_public("static", "docs")
    generate_pages("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    main(basepath)