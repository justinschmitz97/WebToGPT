import os

def process_file(file_path, output_file, root_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    relative_path = os.path.relpath(file_path, root_path)
    with open(output_file, 'a', encoding='utf-8') as outfile:
        outfile.write(f"{relative_path}\n\n\"\"\"\"\n{content}\n\"\"\"\"\n\n")

def walk_through_folder(folder_path, output_file, ignore_files, ignore_extensions, ignore_dirs):
    for root, dirs, files in os.walk(folder_path):
        # Modify the dirs in-place to skip any ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file_name in files:
            if file_name in ignore_files:
                continue  # Skip if the file name is in the ignore list

            _, file_extension = os.path.splitext(file_name)
            if file_extension.lower() in ignore_extensions:
                continue  # Skip if the file extension is in the ignore list

            full_path = os.path.join(root, file_name)
            try:
                process_file(full_path, output_file, folder_path)
            except Exception as e:
                print(f"Error processing file {full_path}: {e}")

# Replace './' with the path to the folder you want to process
folder_path = './'
output_file = '_summary.txt'
# List of filenames to ignore
ignore_files = ['package-lock.json', '.gitignore', '.env.local', 'meta.js', 'global.css', 'next-env.d.ts', 'LICENSE', 'gpt.py', '_summary.txt']
# List of file extensions to ignore (with the dot)
ignore_extensions = ['.xlsx', '.mdx']
# List of directories to ignore
ignore_dirs = ['publications', 'imprint', 'landing', 'public', 'mdx-en', 'node_modules', '.next', '.contentlayer', '.git', 'py_output', ".vercel", "urls", "data"]

# Ensure the output file is empty before we start writing
open(output_file, 'w').close()

# Convert file extensions to lowercase set for consistency in comparison
ignore_extensions = set(ext.lower() for ext in ignore_extensions)

walk_through_folder(folder_path, output_file, ignore_files, ignore_extensions, ignore_dirs)
print(f"The contents of all files have been written to {output_file}")