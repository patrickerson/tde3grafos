
from ast import keyword
from types import NoneType
from filemanipulation.dirs import Dirs
from filemanipulation.file import Files
from model.EmailModel import EmailModel
import json

dirty_data = Dirs("dirty_data")
preprocessing_data = Dirs("preprocessing_data")

sub_dirs = dirty_data.list_subdirs()
counter = 0
wrong_counter=0
wrongfiles = Dirs("preprocessing_data/wrong_files")

# Máximo recursão pro python é 1000, F recursiva
# def recursive_walker(dirs, counter=0, wrong_counter=0):
#     if dirs == []:
#         return counter, wrong_counter
#     file = Files(dirs[0])
#     if file.valid():
#         reader = file.read_file().split("\n")
#         schema = EmailModel()
#         schema.set_schema(
#             id=reader[0].split(": ")[1], 
#             date=reader[1].split(": ")[1],
#             emailFrom=reader[2].split(": ")[1],
#             emailTo=reader[3].split(": ")[1]
#             )

#         dict_to_json = json.dumps(schema.export_dict())
#         if "@" not in schema.emailTo:
#             gen_wrong_file = Files(f"{wrong_counter}.json", data_workdir="preprocessing_data/wrong_data")
#             writer = gen_wrong_file.append_file()
#             writer.write(dict_to_json)
#             writer.write(f"\nfilename: {file.filename}\n")
#             writer.close()
#             return recursive_walker(dirs[1:],counter,wrong_counter+1)
#         else:
#             gen_file = Files(f"{counter}.json", data_workdir="preprocessing_data/ready_data")
#             gen_file.write_file(dict_to_json)
            
#             return recursive_walker(dirs[1:],counter+1,wrong_counter)
#     else:
#         subdirs = Dirs(dirs[0]).list_subdirs()
#         c,w = recursive_walker(subdirs,counter,wrong_counter)
#         # print(dirs)
#         # if len(dirs) == 1:
#         #     return counter,wrong_counter
#         return recursive_walker(dirs[1:], c,w)
        
        
# recursive_walker(["dirty_data"])
subject_keyword="Subject"
len_subject = len(subject_keyword)
def create_file(content, original_file):
    schema = EmailModel()
    counter_to = 3
    emailTo = content[counter_to].split(": ")[1]
    replaced_list = emailTo.replace(" ", "").split(",")
    if emailTo.count(",")>1 and "@" in emailTo:
        if replaced_list[-1] == "":
            replaced_list = replaced_list[:-1]
        counter_to+=1
        while content[counter_to][:len_subject] !=subject_keyword:
            v = content[counter_to].replace(" ", "").split(",")
            if v[-1] == "":
                v = v[:-1]
            for c in v:
                replaced_list.append(c)
            counter_to+=1
        schema.set_schema(
            id=content[0].split(": ")[1], 
            date=content[1].split(": ")[1],
            emailFrom=content[2].split(": ")[1],
            emailTo=replaced_list
        )
        print(counter)
    else:
        schema.set_schema(
            id=content[0].split(": ")[1], 
            date=content[1].split(": ")[1],
            emailFrom=content[2].split(": ")[1],
            emailTo=emailTo
            )

    dict_to_json = json.dumps(schema.export_dict())
    
    if "@" not in schema.emailTo and type(schema.emailTo) != list:
        gen_wrong_file = Files(f"{wrong_counter}.txt", data_workdir="preprocessing_data/wrong_data")
        
        gen_wrong_file.write_file(f"schema: {dict_to_json}\nfilename: {original_file}\n")
        return False

    gen_file = Files(f"{counter}.json", data_workdir="preprocessing_data/ready_data")
    gen_file.write_file(dict_to_json)
    return True
    
for i in sub_dirs:
    new_dir = Dirs(i)
    for j in new_dir.list_subdirs():
        sub_dir = Dirs(j)
        for cabo_criatividade in sub_dir.list_subdirs():
           
            f = Files(cabo_criatividade)
            
            if f.valid():
                reader = f.read_file().split("\n")
                if create_file(reader, f.filename):
                    counter+=1
                else:
                    wrong_counter+=1
            else:
                for sla in Dirs(cabo_criatividade).list_subdirs():
                    f = Files(sla)
                    reader = f.read_file().split("\n")
                    if create_file(reader, f.filename):
                        counter+=1
                    else:
                        wrong_counter+=1
                          
          

