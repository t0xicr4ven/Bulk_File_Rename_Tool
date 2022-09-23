import os
from rename import Rename
## get path of folder
## get list of files in there
## ask what will be the new name

file_path = ""
new_file_name = ""
test_path = "C:\\Users\\t0xic\\OneDrive\Desktop\\Share_With_Work\\"


# Start of program
if __name__ == "__main__":
        print("#########################################################################")
        print("#                         File manipulator                              #")
        print("#               Enter file path e.g. c:\path\path\path                  #")
        print("#                      Rename all files in path                         #")
        print("#                         Rename certain file                           #")
        print("#########################################################################")
        file_path = input("Please enter the path of the folder: ")
        new_file_name = input("Please enter the name you wish to use (e.g. IMAGE): ")

        print(file_path)
        #Check to see if file path is valid
        try:
                #print(os.listdir(test_path))
                Rename.rename_only_certain_file_type(test_path,new_file_name,"txt")
               # Rename.rename_all_files(test_path, new_file_name)
        except FileNotFoundError:
                print("file path not found")



