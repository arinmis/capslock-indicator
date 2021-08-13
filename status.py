import os

bashCommand = "xset q | grep Caps > bash-output.txt" 
os.system(bashCommand)

file = open("bash-output.txt", "r")
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
                
