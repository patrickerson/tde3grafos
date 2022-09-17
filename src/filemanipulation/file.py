from os.path import realpath
from platform import system

class Files():
    
    
    def __init__(self, filename, data_workdir=None):
        """
        Parameters
        --------
            filename: nome do arquivo
            data_workdir: nome do diretório que data estará trabalhando

        Os arquivos não devem conter "/" ou a barra invertida
        exem
        """
        self.relative_system_bar()
        self.workdir =  realpath(f".{self.bar}data")
        if data_workdir is None:
            self.filename = f"{self.workdir}{self.bar}{filename}"
        else:
            self.filename = f"{self.workdir}{self.bar}{data_workdir}{self.bar}{filename}"
        
    
    def read_file(self):
        f = open(self.filename)
        return f.read()


    def relative_system_bar(self):
        my_os = system()
        if my_os.lower() == "windows": 
            # Para de fazer o curso
            self.bar = "\\"
        
        else:
            self.bar = "/"