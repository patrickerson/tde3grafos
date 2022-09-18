
from filemanipulation.file import Files

from filemanipulation.dirs import Dirs
from json import loads
from graph.graph import Graph

from model.EmailModel import EmailModel

clean_data = Dirs("preprocessing_data/ready_data")

G = Graph()

for i in clean_data.list_subdirs():
    f = Files(i)
    file_data = loads(f.read_file())
    node = EmailModel()
    node.set_schema(
        id=file_data['id'],
        date=file_data['date'],
        emailFrom=file_data['emailFrom'],
        emailTo=file_data['emailTo']
    )
    G.add_node(node.emailFrom)
    print(node.emailTo)
    if not type(node.emailTo) is str:
        for email in node.emailTo:
            G.add_node(email)
            G.add_edge(node.emailFrom,email)
    else:
        G.add_node(node.emailTo)
        G.add_edge(node.emailFrom,node.emailTo)

G.print_list_adj()

