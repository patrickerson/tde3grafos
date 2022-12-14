
from src.filemanipulation.file import Files

from src.filemanipulation.dirs import Dirs
from json import loads
from src.graph import Graph

from src.model.EmailModel import EmailModel
from time import perf_counter
clean_data = Dirs("preprocessing_data/ready_data")


def gen_graph(G):
    for i in clean_data.list_subdirs():
        f = Files(i)
        file_data = loads(f.read_file())
        node = EmailModel()
        node.set_schema(
            emailFrom=file_data['emailFrom'],
            emailTo=file_data['emailTo']
        )

        G.add_node(node.emailFrom)
        if not type(node.emailTo) is str:
            for email in node.emailTo:
                G.add_node(email)
                if G.check_edge(node.emailFrom, email):
                    pass
                G.increment_edge(node.emailFrom, email)
        else:
            G.add_node(node.emailTo)
            G.increment_edge(node.emailFrom, node.emailTo)
