
from filemanipulation.file import Files

from filemanipulation.dirs import Dirs
from json import loads
from graph.graph import Graph

from model.EmailModel import EmailModel

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
                G.increment_edge(node.emailFrom,email)
        else:
            G.add_node(node.emailTo)
            G.increment_edge(node.emailFrom,node.emailTo)


if __name__ == "__main__":

    G = Graph()
    gen_graph(G)
    print(f"nodes: {G.n_nodes()}")
    print(f"edges: {G.n_edge()}")
    print()
    G.print_list_adj()
    print(G.great_min_path("sandra.brawner@enron.com", "felicia.beal@enron.com"))
