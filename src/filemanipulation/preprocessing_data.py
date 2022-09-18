from file import Files
from os import listdir
from os.path import isfile

class PreProcessing():

    
    def __init__(self):
        pass

    def list_files(self):
        print([i for i in listdir("./data")])
        pass


if __name__ == "__main__":
    preprocessing = PreProcessing()
    preprocessing.list_files()