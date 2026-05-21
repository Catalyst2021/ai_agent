from functions.get_files_info import get_files_info

test_dir = [".", "pkg", "/bin", "../"]


for dir in test_dir: 
    if dir == ".":
        print(f"Results for current directory:")
    else:
        print(f"Results for '{dir}' directory:")

    print(get_files_info("calculator", dir))