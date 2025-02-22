import os
import shutil

def move_from_static_to_public(source_path: str, destination_path: str) -> None:
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
            shutil.copy(source_item_path, dest_item_path)
        else:
            os.mkdir(dest_item_path)
            move_from_static_to_public(source_item_path, dest_item_path)
