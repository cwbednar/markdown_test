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