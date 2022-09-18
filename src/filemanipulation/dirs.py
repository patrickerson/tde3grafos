from os import listdir
from platform import system
from config import WORKDIR
class Dirs:

    rootdir = WORKDIR
    def __init__(self,workdir):
        self.relative_system_bar()
        self.workdir = workdir
        self.real_workdir = f"{self.rootdir}{self.bar}{self.workdir}"
        


    def relative_system_bar(self):
        my_os = system()
        if my_os.lower() == "windows": 
            # Para de fazer o curso
            self.bar = "\\"
        
        else:
            self.bar = "/"

    def list_subdirs(self):
        
        return [f"{self.workdir}{self.bar}{i}" for i in listdir(self.real_workdir)]

    def list_realpaths_subdir(self):
        return [f"{self.real_workdir}{self.bar}{i}" for i in listdir(self.real_workdir)]
        
if __name__ == "__main__":
    dir = Dirs()
    dir.list_subdirs()