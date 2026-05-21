from functions.get_files_info import get_files_info

#test_dir = [".", "/bin", "../", "main.py"]
test_dir = ["."]

for dir in test_dir: 
    test_res = get_files_info("calculator", dir)
    print(test_res)