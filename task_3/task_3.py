from pathlib import Path
from colorama import  Fore, Style

def display_dir_tree(dir_path):
    path = Path(dir_path)
    
    try:
        items = path.iterdir()
    except PermissionError:
        print('Invalid path')
        return
    
    for item in items:
        if item.is_dir():
            print(f"{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            display_dir_tree(item)
        else:
            print(f"{Fore.GREEN}    🗃️  {item.name}{Style.RESET_ALL}")




