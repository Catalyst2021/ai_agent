from functions.get_files_info import get_files_info

test_cases = [
    ("current directory", "."),
    ("'pkg' directory", "pkg"),
    ("'/bin' directory", "/bin"),
    ("'../' directory", "../"),
]



for label, directory in test_cases: 
    print(f"Result for {label}:")
    print(get_files_info("calculator", directory))