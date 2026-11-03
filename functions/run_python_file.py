import os
import subprocess

def run_python_file (
        working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))

        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(target_dir)

        if is_file == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]

        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=working_directory_abs, capture_output=True, text=True, timeout=30)

        string = ""

        if result.returncode != 0:
            string += f'Process exited with code {result.returncode}\n'

        
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            string += f'No output produced'
            return string
        else:
            if len(result.stdout) > 0:
                string += f'STDOUT: {result.stdout}\n'
            if len(result.stderr) > 0:
                string += f'STDERR: {result.stderr}\n'
        return string

    except Exception as e:
        return f"Error: executing Python file: {e}"