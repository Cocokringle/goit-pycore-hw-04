from pathlib import Path


def total_salary(path):
    file_path = Path(path)
    if file_path.exists() and file_path.is_file():

        with open(path, 'r', encoding='utf-8') as file:
            total_sum=0
            count=0

            for line in file:
                try:
                    name, salary_str = line.strip().split(',')
                    total_sum += int(salary_str)
                    count += 1
                except (ValueError, IndexError):
                    print('Invalid data format')

        if count == 0:
            return 0,0
        
        average_salary = total_sum / count
        return total_sum, average_salary


    else:
        print(f'File {file_path} dose not exist')



total, average = total_salary("./salary_file.txt")
print(f"Total salary: {total}, Average salary: {int(average)}")