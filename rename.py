import os
import pathlib
from tokenize import String


class Rename:

# will return the extension of given file path
    def get_extension_of_file(path):
        return pathlib.Path(path).suffix

# will rename all of the files in the selected folder, with given name
    # pathOfFiles = the given path of where the files are
    # newName = the name users wants the files to be renamed with
    # extensionType = type of file type e.g .txt .png .jpeg
    def rename_all_files(pathOfFiles,newName,extensionType=""):
        count = 1
        #iterate over all files within path
        for file in os.listdir(pathOfFiles):
            #get original absolute path
            absolute_name = pathOfFiles + file
            if extensionType == "":
                extensionType = pathlib.Path(absolute_name).suffix
            #new absolute path
            new_path = pathOfFiles + newName + "_" + str(count) + extensionType   
            os.rename(absolute_name, new_path)
            count += 1

    # this func will only rename the selected file types
    def rename_only_certain_file_type(filePath,newName,fileType):
        count = 1
        #iterate over files in path and only name the selected the file type
        for file in os.listdir(filePath):
            fullPath = filePath + file
            currentExtension = pathlib.Path(fullPath).suffix
            currentExtension = currentExtension.strip(".")
            #get file type
            if currentExtension == fileType:
                new_path = filePath + newName + "_" + str(count) + pathlib.Path(fullPath).suffix
                os.rename(fullPath,new_path)
                count += 1

            



