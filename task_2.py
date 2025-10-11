from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)
    cats_data = []
    if file_path.exists() and file_path.is_file():
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id,name,age = line.strip().split(',')

                    cat_info={
                        "id": cat_id,
                        "name":name,
                        "age":int(age)
                    }

                    cats_data.append(cat_info)

                except (ValueError, IndexError):
                    print('Invalid data format')

        return cats_data
    
    else:
        print(f'File {file_path} dose not exist')
        return []


cats_list = get_cats_info("./cats_file.txt")
print(cats_list)
