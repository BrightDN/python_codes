import os
import shutil
from src.file_operations.generate_page import generate_page

def generate_pages(source_path: str, template_file_path: str, destination_path: str, basepath: str) -> None:
    """
    This function takes in 2 parameters and moves all files and directories from the source_path parameter into the destionation_path parameter.

    Parameters:
    source_path (str) : This parameter defines the path of which we will copy its contents from
    destionation_path (str) : This parameter defines the path which we will copy the contents into

    Returns:
    Nothing, this function modifies files
    """
    
    
    for item in os.listdir(source_path):
        # Create full source path for this item
        source_item_path = os.path.join(source_path, item)
        # Create full destination path for this item
        dest_item_path = os.path.join(destination_path, item)
        
        if os.path.isfile(source_item_path):
            dest_item_path = os.path.join(destination_path, item.replace('.md', '.html'))
            generate_page(source_item_path, template_file_path, dest_item_path, basepath)
        else:
            # Handle directories
            dest_item_path = os.path.join(destination_path, item)
            # Create the directory if it doesn't exist
            if not os.path.exists(dest_item_path):
                os.mkdir(dest_item_path)
            # Recursively process the subdirectory
            generate_pages(source_item_path, template_file_path, dest_item_path, basepath)