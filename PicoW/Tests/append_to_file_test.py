import os

def append_to_file(item_to_append, to_file, delim):
    _txt = open(to_file, 'at')
    _txt.write(f'{item_to_append}{delim}')
    _txt.close()


append_to_file("Add Me", "test_file.txt", "\n")
