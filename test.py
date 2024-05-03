from os import listdir,path

sample_name = "log_"
folder_path = "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/log"
log_list = listdir(folder_path)
num_log = len(log_list) + 1
file_name = sample_name+str(num_log)+str(".txt")
file_path = path.join(folder_path,file_name)
print(file_path)
try:
    # Try to open the file in exclusive creation mode ('x')
    with open(file_path, 'x') as file:
        # If the file doesn't exist, it will be created
        print(f"File created: {file_path}")
except FileExistsError:
    # If the file already exists, print a message
    print(f"File already exists: {file_path}")