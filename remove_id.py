import os 
import re

# ID regex pattern
PATTERN = r'( |%20)[0-9a-f]{32}'  # in md, the space is encoded as %20
ROOT_DIR = os.getcwd()

def treat_directory(dir_path):
    # treat all files in it
    # treat subdirectories recursively 
    all_items = os.listdir(dir_path)
    for f in all_items:
        item_path = os.path.join(dir_path, f)
        if os.path.isfile(item_path):
            treat_file(item_path)
        elif os.path.isdir(item_path):
            treat_directory(item_path)
    change_base_name(dir_path)

def treat_file(file_path):
    # change file name
    # if the file is md (or something else?), replace all id pattern by empty string
    if file_path.endswith(".md"):
        with open(file_path, "r") as f:
            content = f.read()
            new_content = re.sub(PATTERN, "", content)
        with open(file_path, "w") as f:
            f.write(new_content)
            print(f"changed content of {file_path}")
    change_base_name(file_path)

def change_base_name(path):
    base_name = os.path.basename(path)
    parent_dir_name = os.path.dirname(path)
    new_base_name = re.sub(PATTERN, "", base_name)
    new_path = os.path.join(parent_dir_name, new_base_name)
    os.rename(path, new_path)
    print(f"renamed {path} to {new_path}")

if __name__ == "__main__":
    print(ROOT_DIR)
    treat_directory(ROOT_DIR)
    print("All done!")
