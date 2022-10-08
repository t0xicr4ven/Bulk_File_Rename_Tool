import os

class Travel:
    print("this is the travel class")



    #get the current working directory
    def current_work_dir():
        return os.getcwd()

    #change the current dir
    def change_dir(user_input):
        #get current dir just incase something goes wrong
        pwd = os.getcwd()
        try:
            os.chdir(user_input)
        except:
            print("Something went wrong trying to change path")
        finally:
            #if error put back in current dir
            os.chdir(pwd)
    
    #list files in dir
    def list_contents_dir():
        return os.listdir()

