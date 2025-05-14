def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as my_file:
        my_file.write(file_content)
        # Write the content to the file
    
    

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as my_file:
        my_file.write(append_content)
        # Append the content to the file

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as my_file:
       return my_file.read()
        # Read the content of the file
    
