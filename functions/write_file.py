import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

        valid_target_dir = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if valid_target_dir == False:
            return f'Error: Cannot write to "{file_path}" as is it outside the permitted working directory'

        is_dir = os.path.isdir(target_file)

        if is_dir == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)
  
        with open(target_file, "w") as file:
            file.write(content)

        return f'Successfully wrote "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write content to a file at file_path, creating the file and any parent directories if needed. Overwrites existing contents.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to target file, relative to the working directory.",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the file"
                },
            },
            "required": ["file_path", "content"]
        },
    },
}