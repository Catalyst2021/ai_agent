import os 
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        
        if args: 
            command.extend(args)
        
        execute_python = subprocess.run(command,
                                        cwd=working_dir_abs,
                                        capture_output=True,
                                        timeout=30,
                                        text=True)
        
        output_string = ""

        if execute_python.returncode != 0:
            output_string += f'Process exited with code {execute_python.returncode}'
        
        if execute_python.stdout and execute_python.stderr:
            output_string += f"No output produced"

        output_string += f'STDOUT:{execute_python.stdout} STDERR:{execute_python.stderr}'

        return output_string        

        
    except Exception as e: 
        return f"Error: executing Python file: {e}"