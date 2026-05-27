import os 
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="write_file",
    description="Write the contents to a file in specified file relative to the working directory, providing a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path","content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path to write file contents to, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to write to file, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_path):
            return f'Error: "{file_path}" as it is a directory'

        os.makedirs(working_dir_abs, exist_ok= True)

        with open(target_path, "w") as f:
            f.write(content)
    
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e: 
        return f'Error: {e}'