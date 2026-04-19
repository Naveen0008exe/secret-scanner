import os
def walk_files(folder):
    found_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            found_files.append(full_path)

    return found_files
        

          
