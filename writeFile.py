file_name = "example.txt"

with open(file_name, 'w') as file:
    file.write("Hello, this is an example of writing to a file in Python.\n")
    file.write("We can write multiple lines.\n")

print(f"Content written to {file_name} successfully.")
