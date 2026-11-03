import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        is_dir = os.path.isdir(target_dir)

        if is_dir == False:
            return f'Error: "{directory}" is not a directory'

        if valid_target_dir == True:

            string = ""

            for i in os.listdir(target_dir):
                name = i
                file_size = os.path.getsize(os.path.normpath(os.path.join(target_dir, i)))
                is_directory = os.path.isdir(os.path.normpath(os.path.join(target_dir, i)))
                string = string + f"- {name}: file_size={file_size} bytes, is_dir={is_directory}\n"
            
            return string

            # return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"
