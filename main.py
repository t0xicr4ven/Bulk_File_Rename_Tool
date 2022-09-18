from cgi import test
import os
## get path of folder
## get list of files in there
## ask what will be the new name


file_path = ""
new_file_name = ""

file_path = input("Please enter the path of the folder: ")
new_file_name = input("Please enter the name you wish to use (e.g. IMAGE): ")


# Functions

def rename_all_files(path,name):
    count = 1
    for file in os.listdir(path):
        #get original absolute path
        absolute_name = path + file

        #new absolute path
        new_path = path + new_file_name + "_" + str(count) + ".txt"   
#TODO need a way to put original file type at the end

        os.rename(absolute_name, new_path)
        count += 1



# Start of program

test_path = "C:\\Users\\t0xic\\OneDrive\Desktop\\Share_With_Work\\"
print(file_path)

#Check to see if file path is valid
try:
    print(os.listdir(test_path))
    rename_all_files(test_path, new_file_name)
except FileNotFoundError:
        print("file path not found")





# old_name = "C:\\Users\\t0xic\\OneDrive\Desktop\\Share_With_Work\\test_note.txt"
# new_name = "C:\\Users\\t0xic\\OneDrive\Desktop\\Share_With_Work\\new_name_note.txt"

#rename file

# os.rename(old_name, new_name)


