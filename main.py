import os
import shutil
from src.file_operations.move_from_static_to_public import move_from_static_to_public

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

    if os.path.exists("static"):
        move_from_static_to_public("static", "public")

main()

