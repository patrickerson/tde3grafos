
from filemanipulation.file import Files

from filemanipulation.dirs import Dirs
from json import loads
from graph.graph import Graph

from model.EmailModel import EmailModel
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
                # G.add_node(email)
                if G.check_edge(node.emailFrom, email):
                    pass
                G.increment_edge(node.emailFrom,email)
        else:
            G.add_node(node.emailTo)
            G.increment_edge(node.emailFrom,node.emailTo)


if __name__ == "__main__":

    timer = perf_counter()
    G = Graph()
    gen_graph(G)
    timer_finish = perf_counter()
    print(f"generate graph: {timer_finish-timer}")
    print(f"nodes: {G.n_nodes()}")
    
    print(f"edges: {G.n_edge()}")
    
    
    timer = perf_counter()
    result = G.DFS("sandra.brawner@enron.com","felicia.beal@enron.com")
    timer_finish = perf_counter()
    print(f"DFS: {timer_finish-timer}")

    timer = perf_counter()
    result = G.BFS("sandra.brawner@enron.com","felicia.beal@enron.com")
    timer_finish = perf_counter()
    print(f"BFS: {timer_finish-timer}")
    
    G.print_graph_adj()
    # print(G.Dijkstra("sandra.brawner@enron.com", "felicia.beal@enron.com"))
    print(G.dijkstra("sandra.brawner@enron.com")[0])
    f = open("output.txt", "w")
    f.write(G.dijkstra_warshall("sandra.brawner@enron.com", 1).__str__())