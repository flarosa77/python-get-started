import os

path = '/Users/flarosa/Desktop/files/'

stringa = 'file_'

# Ottengo la lista dei file che si trovano nel path
list_files = os.listdir(path)
print(list_files)

# scorro la lista dei file
for name_file in list_files:
    new_name = name_file.replace(stringa, "")
    os.rename(path + name_file, path + new_name)


list_files = os.listdir(path)
print(list_files)






