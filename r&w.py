def modify_file():
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        modified = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified)

        print("File has been modified and saved as 'output.txt'")
    except Exception as e:
        print(f"Something went wrong: {e}")


def safe_file_read():
    filename = input("iput.text: ")

    try:
        with open(filename, "r") as f:
            print("\nFile Content:")
            print(f.read())
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except PermissionError:
        print(f"You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    print("=== File Read & Write Challenge ===")
    modify_file()

    print("\n=== Error Handling Lab ===")
    safe_file_read()

    print("\nYou have now practiced reading, writing, and error handling with files in Python!")
