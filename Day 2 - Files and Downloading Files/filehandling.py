# fname = "hello.txt"
# file_object = open(fname,"w")
# file_object.write("Hello World")
# file_object.close()

# with open(fname,"w") as file_object:
#     file_object.write("Hello World Again!!")

# with open(fname,'r') as f:
#     print(f.read())
import os
this_file_path = os.path.abspath(__file__)
# print(this_file_path)#/home/doomguy/Desktop/Coding/Python/Files/filehandling.py
BASE_DIR = os.path.dirname(this_file_path)
# print(BASE_DIR)#/home/doomguy/Desktop/Coding/Python/Files
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
# print(ENTIRE_PROJECT_DIR)#/home/doomguy/Desktop/Coding/Python
email_txt = os.path.join(BASE_DIR,"templates","email.txt")
content = ""
with open(email_txt,'r') as f:
    content = f.read()

print(content.format(name = 'Rohit'))