
from ast import keyword
import os
from types import NoneType
from filemanipulation.dirs import Dirs
from filemanipulation.file import Files
from model.EmailModel import EmailModel
import json





dirty_data = Dirs("dirty_data")
preprocessing_data = Dirs("preprocessing_data")
path_wrong_data = "preprocessing_data/wrong_data"
path_ready_data = "preprocessing_data/ready_data"
wrongfiles = Dirs(path_wrong_data)
readydata = Dirs(path_ready_data)


def gen_dirs():
    dirty_data.make_dir()
    preprocessing_data.make_dir()
    wrongfiles.make_dir()
    readydata.make_dir()




def clean_old_files():
    for file in wrongfiles.list_realpaths_subdir():
        os.remove(file)
    for file in readydata.list_realpaths_subdir():
        os.remove(file)




def create_file(content):
    schema = EmailModel()
    counter_to = 3
    to=content[counter_to].split(": ")[0]
    emailTo = content[counter_to].split(": ")[1]
    if not "To" in to:
        return None
    if emailTo == "":
        counter_to+=2
        emailTo= content[counter_to]
    if emailTo.count(",")>1 and "@" in emailTo:
        replaced_list = emailTo.replace(" ", "").split(",")
        if replaced_list[-1] == "":
            replaced_list = replaced_list[:-1]
        counter_to+=1
        while content[counter_to][:len_subject] !=subject_keyword:
            v = content[counter_to].replace(" ", "").replace("\t", "").split(",")
            if v[-1] == "":
                v = v[:-1]
            for c in v:
                replaced_list.append(c)
            counter_to+=1
        schema.set_schema(
            emailFrom=content[2].split(": ")[1],
            emailTo=replaced_list
        )
    else:
        schema.set_schema(
            emailFrom=content[2].split(": ")[1],
            emailTo=emailTo
            )

    dict_to_json = json.dumps(schema.export_dict())
    if "@" not in schema.emailTo and type(schema.emailTo) != list:
        gen_wrong_file = Files(f"{wrong_counter}.txt", data_workdir=path_wrong_data)
        var = "\n".join(reader)
        gen_wrong_file.write_file(f"schema: {dict_to_json}\nfilename: {var}\n")
        print(to)
        return False

    gen_file = Files(f"{counter}.json", data_workdir=path_ready_data)
    gen_file.write_file(dict_to_json)
    return True
    

gen_dirs()
sub_dirs = dirty_data.list_subdirs()
counter = 0
wrong_counter=0
subject_keyword="Subject"
len_subject = len(subject_keyword)
for i in sub_dirs:
    new_dir = Dirs(i)
    for j in new_dir.list_subdirs():
        sub_dir = Dirs(j)
        for cabo_criatividade in sub_dir.list_subdirs():
           
            f = Files(cabo_criatividade)
            
            if f.valid():
                reader = f.read_file().split("\n")
                create = create_file(reader)
                if create == None:
                    continue
                elif create:
                    counter+=1
                else:
                    wrong_counter+=1
            else:
                for sla in Dirs(cabo_criatividade).list_subdirs():
                    f = Files(sla)
                    reader = f.read_file().split("\n")
                    create = create_file(reader)
                    if create == None:
                        pass
                    elif create:
                        counter+=1
                    else:
                        wrong_counter+=1
                          
print(f"ready data files: {counter}")
print(f"wrong data files: {wrong_counter}")
