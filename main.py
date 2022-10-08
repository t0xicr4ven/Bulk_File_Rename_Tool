import os
from rename import Rename
from travel import Travel

## get path of folder
## get list of files in there
## ask what will be the new name

file_path = ""
new_file_name = ""
test_path = "C:\\Users\\t0xic\\OneDrive\Desktop\\Share_With_Work\\"
prompt_text = "CoDe:> "
keep_it_up = True

# Start of program
if __name__ == "__main__":
        print("#########################################################################")
        print("#                      Python Command Line                              #")
        print("#                       type help for help                              #")
        print("#                       type quit to exit                               #")
        print("#                                                                       #")
        print("#########################################################################")
       
        #start the input loop
        while keep_it_up:
                user_says = input(prompt_text)
                #check if input is quit before moving forward
                if user_says == "quit":
                        keep_it_up = False
                        print("Thank you please come back soon")
                else:
                        print(user_says)




        file_path = input("Please enter the path of the folder: ")
        new_file_name = input("Please enter the name you wish to use (e.g. IMAGE): ")

        print(file_path)

        print("This is the current working dir:::: " + Travel.current_work_dir())
        file_list_fm_path = Travel.list_contents_dir()

        print("This is the dir list::::::: ")  
        print(file_list_fm_path)
        #Check to see if file path is valid
        try:
                #print(os.listdir(test_path))
                Rename.rename_only_certain_file_type(test_path,new_file_name,"txt")
               # Rename.rename_all_files(test_path, new_file_name)
        except FileNotFoundError:
                print("file path not found")



