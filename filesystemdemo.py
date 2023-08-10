
import os
import stat
import uuid

def create_file():
    file_name = input("Enter the file name including full path: ")
    if os.path.exists(file_name):
        print("File already exists.")
    else:
        tag = str(uuid.uuid4())[:8]  # Generate a unique tag
        with open(file_name, 'w') as f:
            f.write("Tag: " + tag + "\n")
        file_size = os.path.getsize(file_name)  # Get the file size in bytes
        print(f"File created successfully. Tag: {tag}, Size: {file_size} bytes")


def read_file():
    file_name = input("Enter the file name: ")
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            content = f.read()
            print("File content:")
            print(content)
    else:
        print("File not found.")


def write_file():
    file_name = input("Enter the file name: ")
    if os.path.exists(file_name):
        with open(file_name, 'a') as f:
            data = input("Enter the data to write: ")
            f.write(data)
            print("Data written successfully.")
    else:
        print("File not found.")


def create_and_write_to_file():
    file_name = input("Enter the file name including full path: ")
    if os.path.exists(file_name):
        print("File already exists.")
    else:
        with open(file_name, 'w') as f:
            print("File created successfully.")
        with open(file_name, 'a') as f:
            data = input("Enter the data to write: ")
            f.write(data)
            print("Data written successfully.")


def delete_file():
    file_name = input("Enter the file name: ")
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File deleted successfully.")
    else:
        print("File not found.")


def create_directory():
    dir_name = input("Enter the directory name: ")
    if os.path.exists(dir_name):
        print("Directory already exists.")
    else:
        os.mkdir(dir_name)
        print("Directory created successfully.")


def create_directory_create_file():
    dir_name = input("Enter the directory name: ")
    if os.path.exists(dir_name):
        print("Directory already exists.")
    else:
        os.mkdir(dir_name)
        print("Directory created successfully.")
    file_name = input("Enter the file name including full path: ")
    if os.path.exists(file_name):
        print("File already exists.")
    else:
        with open(file_name, 'w') as f:
            print("File created successfully.")


def create_directory_create_file_and_write_to_file():
    dir_name = input("Enter the directory name: ")
    if os.path.exists(dir_name):
        print("Directory already exists.")
    else:
        os.mkdir(dir_name)
        print("Directory created successfully.")
    file_name = input("Enter the file name including full path: ")
    if os.path.exists(file_name):
        print("File already exists.")
    else:
        with open(file_name, 'w') as f:
            print("File created successfully.")
        with open(file_name, 'a') as f:
            data = input("Enter the data to write: ")
            f.write(data)
            print("Data written successfully.")


def list_files_in_directory():
    dir_name = input("Enter the directory name: ")
    if os.path.exists(dir_name):
        files = os.listdir(dir_name)
        print("Files in directory:")
        for file in files:
            print(file)
            print("Permission are as follows:")
            if os.access(file, os.R_OK):
                print(f"Read permissions granted.")
            else:
                print(f"Read permissions not granted.")
            if os.access(file, os.W_OK):
                print(f"Write permissions granted.")
            else:
                print(f"Write permissions not granted.")
            if os.access(file, os.X_OK):
                print(f"Execute permissions granted.")
            else:
                print(f"Execute permissions not granted.")
    else:
        print("Directory not found.")


def search_file_in_directory():
    dir_name = input("Enter the directory name: ")
    if os.path.exists(dir_name):
        file_name = input("Enter the file name to search: ")
        if file_name in os.listdir(dir_name):
            print("File found.")
        else:
            print("File not found.")
    else:
        print("Directory not found.")


def delete_dir():
    dir_name = input("Enter the name of the directory:")
    if os.path.exists(dir_name):
        os.rmdir(dir_name)
        print("Directory has been deleted successfully.")
    else:
        print("Directory does not exist.")




def change_file_permissions(file_path, mode):
    try:
        os.chmod(file_path, mode)
        print("File permissions changed successfully.")
    except OSError as e:
        print("Error while changing file permissions:", str(e))


def change_perm():
    file_path = input("Enter the file path: ")
    if os.path.exists(file_path):
        mode_input = input("Enter the new file permissions in octal format (e.g., '755', '644'): ")
        try:
            mode = int(mode_input, 8)  # Convert octal string to integer
            change_file_permissions(file_path, mode)
            print("File permissions changed successfully.")
        except ValueError:
            print("Invalid octal format. Please enter a valid octal number.")
    else:
        print("File not found.")


def show_permissions():
    file_path = input("Enter the file path: ")
    if os.path.exists(file_path):
        try:
            # Get the file status
            file_status = os.stat(file_path)

            # Decode file mode and convert to a string representation
            mode = stat.filemode(file_status.st_mode)
            
            # Extract tag from the file content
            with open(file_path, 'r') as f:
                content = f.read()
                tag = content.split('\n')[0].replace("Tag: ", "")
            
            print(f"File Path: {file_path}")
            print(f"Permissions of {file_path}: {mode}")
            print(f"Tag: {tag}")
        except OSError as e:
            print("Error while getting file permissions:", str(e))
    else:
        print("File not found.")


def show_menu():
    print("File System Menu:")
    print("1. Create File   ", "   2. Read File   ", "          3. Write to File   ", "   4. Create and write to file")
    print("5. Delete File   ", "   6. Create Directory   ", "   7. Create Directory and create file")
    print("8. Create Directory and create file and write to file   ",  "     9. List Files in Directory")
    print("10. Search File in Directory   ", "   11. Delete Directory  ", "12. Change permission")
    print("13. show file permission "," 14. EXIT ")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            write_file()
        elif choice == '4':
            create_and_write_to_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            create_directory()
        elif choice == '7':
            create_directory_create_file()
        elif choice == '8':
            create_directory_create_file_and_write_to_file()
        elif choice == '9':
            list_files_in_directory()
        elif choice == '10':
            search_file_in_directory()
        elif choice == '11':
            delete_dir()
        elif choice == '12':
            change_perm()
        elif choice == '13':
            show_permissions()
        elif choice == '14':
            print("Exiting...")
    
        else:
            print("Invalid choice. Please try again.")
