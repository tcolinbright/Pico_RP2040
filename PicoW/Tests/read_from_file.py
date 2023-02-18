import os

def read_file_into_memory(input_file, delim):
    '''Reads file into a list splitting on delim. Returns list'''
    my_file = open(input_file, "r") # this is the file to read
    data = my_file.read() # reading the file
    new_list = data.split(delim) # split items in file by delim
    my_file.close() # close the file to prevent corruption
    return new_list


read_in_list = read_file_into_memory('test_file.txt', "\n")
print(len(read_in_list) - 1) # -1 acounts for blank new line