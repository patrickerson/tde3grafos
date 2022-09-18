
from filemanipulation.dirs import Dirs
from filemanipulation.file import Files
from model.EmailModel import EmailModel
import json

dirty_data = Dirs("dirty_data")
preprocessing_data = Dirs("preprocessing_data")

sub_dirs = dirty_data.list_subdirs()
counter = 0

for i in sub_dirs:
    new_dir = Dirs(i)
    for j in new_dir.list_subdirs():
        sub_dir = Dirs(j)
        for cabo_criatividade in sub_dir.list_subdirs():
           
            f = Files(cabo_criatividade)
            
            if not f.valid():
                for sla in Dirs(cabo_criatividade).list_subdirs():
                    f = Files(sla)
                    reader = f.read_file().split("\n")
                    schema = EmailModel()
                    schema.set_schema(
                        id=reader[0].split(": ")[1], 
                        date=reader[1].split(": ")[1],
                        emailFrom=reader[2].split(": ")[1],
                        emailTo=reader[3].split(": ")[1]
                        )
                    gen_file = Files(f"{counter}.json", data_workdir="preprocessing_data")
                    dict_to_json = json.dumps(schema.export_dict())

                    gen_file.write_file(dict_to_json)
                    counter+=1
                          
            reader = f.read_file().split("\n")
            schema = EmailModel()
            schema.set_schema(
                id=reader[0].split(": ")[1], 
                date=reader[1].split(": ")[1],
                emailFrom=reader[2].split(": ")[1],
                emailTo=reader[3].split(": ")[1]
                )
            gen_file = Files(f"{counter}.json", data_workdir="preprocessing_data")
            dict_to_json = json.dumps(schema.export_dict())

            gen_file.write_file(dict_to_json)
            counter+=1

