import sys
from pathlib import Path
from task_3 import display_dir_tree

def main():
    root_path_str = sys.argv[1]
    root_path = Path(root_path_str)
    if not root_path.exists() or not root_path.is_dir():
        print('Error: invalid path')
    display_dir_tree(root_path)

main()