import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))

        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        if valid_target_dir == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(target_dir)

        if is_file == False:
            return f'Error: File not found or is not a regular file "{file_path}"'

        with open(target_dir, "r") as file:
            contents = file.read(MAX_CHARS)

            if file.read(1):
                contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
            return contents

    except Exception as e:
        return f"Error: {e}"

    
    
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Grab a file from a file path and return its contents. If content > 10,000 characters function will return the first 10,000 characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the target file, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}