import os
import random

fd = r"C:/alphabet/organized"
os.chdir(fd)
#print os.getcwd()
file_list = os.listdir(fd)


def create_secret():
    for filename in file_list:
        os.rename(filename, str(random.randrange(40)) + filename)
#create_secret()

def reveal_secret():
    for filename in file_list:
        os.rename(filename, filename.translate(None, "0123456789"))
reveal_secret()
