from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")


test_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]


for working_dir, file_path in test_cases: 
    print(f"\n--- get_file_content({working_dir!r}, {file_path!r}) ---")
    print(get_file_content(working_dir, file_path))



