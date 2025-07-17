
# File read operation
def read_file():
    try:
        with open('files/diken.txt', 'r') as file:
            content = file.read()
            file.close()
        return content
    except FileNotFoundError:
        return "File 'diken.txt' not found!"

print(read_file())

def create_and_read_file():
    # Create the file with some content
    try:
        with open('files/diken.txt', 'w') as file:
            file.write("Hello, this is Diken's file!\nThis is line 2.")
            file.close()
    except IOError as e:
        return f"An error occurred while writing to the file: {e}"


    # Now read the file
    with open('files/diken.txt', 'r') as file:
        content = file.read()
        file.close()
    return content

create_and_read_file()


def append_file():
    try:
        with open('files/diken.txt', 'a') as file:
            file.write("\nThis is an appended line.")
            file.close()
    except IOError as e:
        return f"An error occurred while appending to the file: {e}"

    # Now read the file to see the appended content
    return read_file()


print(append_file())