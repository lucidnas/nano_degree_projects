import os
import random

fd = r"C:/alphabet/organized"
os.chdir(fd)
file_list = os.listdir(fd)
print file_list
for filename in file_list:
    os.rename(filename, str(random.randrange(40)) + filename)
print os.getcwd()





##print [''.join(),i)) for i in file_list]

##
##def organize_files:
##    for filename in file_list:
##        os.rename(filename, filename.transtlate(None, "1..9")
##    return
