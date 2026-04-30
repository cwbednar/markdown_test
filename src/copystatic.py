import os
import shutil 

def delete_and_replace(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    os.mkdir(dest)
    inventory = os.listdir(source)

    for item in inventory:
        source_path = os.path.join(source, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            delete_and_replace(source_path, dest_path)

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)