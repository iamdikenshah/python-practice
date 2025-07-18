import os
# Get the current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)
# Create a new directory
# os.mkdir("new_directory") # creates only one level of directory
# os.makedirs("path/to/new_directory") # creates nested directories
# Change the current directory
# os.chdir("new_directory")
# List files and directories in a directory
files = os.listdir(".") # "." represents current directory
print("Files in current directory:", files)
# Remove a file or directory
# os.remove("my_file.txt")
# os.rmdir("new_directory") # removes empty directory
# shutil.rmtree("path/to/new_directory") # removes non-empty directory (use w
# Rename a file or directory
# os.rename("old_name.txt", "new_name.txt")

# Check if a file or directory exists
if os.path.exists("my_file.txt"):
    print("File exists")

# Join path components in a platform-independent way
path = os.path.join("folder", "subfolder", "file.txt")
print("Joined path:", path)




import shutil
# Copy a file
# shutil.copy("my_file.txt", "my_file_copy.txt")
# Move a file or directory
# shutil.move("my_file.txt", "new_directory/")