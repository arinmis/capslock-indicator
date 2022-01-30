import os

ROOT_DIR = os.path.dirname(__file__)
data_file_path = os.path.join(ROOT_DIR, 'bash-output.log')

os.system("xset q | grep Caps > " + data_file_path)

file = open(data_file_path, "r")
# read the line
line = file.read()

# remove whitespaces and make lowercase
line = "".join(line.split()).lower()

array = line.split(':')

# return true if capslock on 
def get_capslock_status():
    for index in range(len(array)):
        if index + 1 < len(array) and array[index] == "capslock":
            # filter capslock status
            status =  array[index + 1]
            status =  "".join([i for i in status if not i.isdigit()])
            if status == "off":
                return False
            return True
                
