file_name = "example.txt"

try:
    with open(file_name, 'r') as file:
        content = file.read()
        
        print("File Content:\n")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
