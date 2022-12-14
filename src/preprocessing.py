import os
from src.filemanipulation.dirs import Dirs
from src.filemanipulation.file import Files
from src.model.EmailModel import EmailModel

import json


class Preprocessing():

    dirty_data = Dirs("dirty_data")
    preprocessing_data = Dirs("preprocessing_data")
    path_wrong_data = "preprocessing_data/wrong_data"
    path_ready_data = "preprocessing_data/ready_data"
    wrongfiles = Dirs(path_wrong_data)
    readydata = Dirs(path_ready_data)
    counter = 0
    wrong_counter = 0
    subject_keyword = "Subject"
    len_subject = len(subject_keyword)

    def __init__(self):
        pass

    def gen_dirs(self):
        self.dirty_data.make_dir()
        self.preprocessing_data.make_dir()
        self.wrongfiles.make_dir()
        self.readydata.make_dir()

    def clean_old_files(self):
        for file in self.wrongfiles.list_realpaths_subdir():
            os.remove(file)
        for file in self.readydata.list_realpaths_subdir():
            os.remove(file)

    def parser_email(self, email):
        if "<" in email:
            email = email.split("<")[1].replace(">", "")
        if "pr <.palmer" in email:
            print(email)
        return email

    def create_file(self, content):
        schema = EmailModel()
        counter_to = 3
        to = content[counter_to].split(": ")[0]
        emailTo = content[counter_to].split(": ")[1]

        if not "To" in to:
            return
        if emailTo == "":
            counter_to += 2
            emailTo = content[counter_to]
        if emailTo.count(",") >= 1 and "@" in emailTo:
            replaced_list = emailTo.replace(" ", "").split(",")
            if replaced_list[-1] == "":
                replaced_list = replaced_list[:-1]
            counter_to += 1
            while content[counter_to][:self.len_subject] != self.subject_keyword:
                v = content[counter_to].replace(
                    " ", "").replace("\t", "").split(",")
                if v[-1] == "":
                    v = v[:-1]
                for c in v:

                    replaced_list.append(c)
                counter_to += 1

            parsed_list = []
            for i in replaced_list:
                parsed_list.append(self.parser_email(i))
            schema.set_schema(
                emailFrom=self.parser_email(content[2].split(": ")[1]),
                emailTo=parsed_list
            )
        else:
            parsed_email = self.parser_email(emailTo)
            schema.set_schema(
                emailFrom=self.parser_email(content[2].split(": ")[1]),
                emailTo=parsed_email
            )
        dict_to_json = json.dumps(schema.export_dict())
        c1 = "@" not in schema.emailTo
        c2 = type(schema.emailTo)
        c3 = "," in schema.emailTo

        if c1 and c2 != list or c3:
            gen_wrong_file = Files(
                f"{self.wrong_counter}.txt", data_workdir=self.path_wrong_data)
            var = "\n".join(content)
            gen_wrong_file.write_file(
                f"schema: {dict_to_json}\nfilename: {var}\n")
            self.wrong_counter += 1
            return False

        filename = f"{self.counter}.json"

        gen_file = Files(filename, data_workdir=self.path_ready_data)

        gen_file.write_file(dict_to_json)
        self.counter += 1
        return True

    def start(self):
        print("teste")
        for lvl1 in self.dirty_data.list_subdirs():
            new_dir = Dirs(lvl1)
            for lvl2 in new_dir.list_subdirs():
                sub_dir = Dirs(lvl2)
                for lvl3 in sub_dir.list_subdirs():

                    f = Files(lvl3)

                    if f.valid():
                        reader = f.read_file().split("\n")
                        self.create_file(reader)
                    else:
                        for lvl4 in Dirs(lvl3).list_subdirs():
                            f = Files(lvl4)
                            reader = f.read_file().split("\n")
                            self.create_file(reader)
        self.print_file_conters()

    def print_file_conters(self):
        print(f"ready data files: {self.counter}")
        print(f"wrong data files: {self.wrong_counter}")
