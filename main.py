from src.preprocessing import Preprocessing
from src.create_graph import  gen_graph
from src.graph import Graph
from time import perf_counter


def print_lines():
    print("-"*100)
    print("\n")

def formated_print(text, argument):
    print(f"{text}: {argument}")

def rank_print(text, list_rank):
    print("\n")
    print(text.upper())
    counter = 1
    for i in list_rank:
        print(f"{counter}. {i[0]}  {i[1]}")
        counter+=1
    print("\n")

def menu():
    print("1. Informações gerais do grafo")
    print("2. Busca em profundidade")
    print("3. Busca em largura")
    print("4. Vértices a um distância D")
    print("5. Diametro do grafo")
    print("6. Sair")

def generic_infos():
    print("INFORMAÇÕES GERAIS DO GRAFO")
    formated_print("nodes number", G.n_nodes())
    formated_print("edges number", G.n_edge())
    rank_print("20 maior saída", G.maior20saida())
    rank_print("20 maior entrada", G.maior20entrada())

def search_view(function):
    source_node = input("vértice de origem: ")
    destiny_node = input("vertice de destino: ")
    result = function(source_node, destiny_node)
    # result = function("sandra.brawner@enron.com", "felicia.beal@enron.com")
    
    counter=1
    if result[0]:
        for i in result[1]:
            print(f"{counter}.{i}")
            counter+=1
    print("É possível alcançar?")
    print(result[0])
def dfs_view():
    print("BUSCA EM PROFUNDIDADE")
    search_view(G.DFS)

def bfs_view():
    print("BUSCA EM largura")
    search_view(G.BFS)

def distance_d():
    print("DISTANCIA D")
    source_node = input("vértice de origem :")
    distance = input("distância: ")
    print(G.dijkstra_warshall(source_node, int(distance)))
print("welcome!")
preprocessing_input = input("PREPARADOR OS DADOS? Y/Anything else ")


def dijkstra():
    source_node = input("vértice de origem: ")
    destiny_node = input("vertice de destino: ")
    cost = G.dijkstra(source_node)
    print(G.djijkstra_min_path(destiny_node, cost))
    pass

if preprocessing_input.upper() == "Y":
    print("teste")
    preprocessing = Preprocessing()
    preprocessing.clean_old_files()
    preprocessing.gen_dirs
    preprocessing.start()

    
G = Graph()
gen_graph(G)




G.print_graph_adj()

print("GRAFO GERADO")
print_lines()
opts = [
    generic_infos, 
    dfs_view, 
    bfs_view,
    distance_d,
    dijkstra

]
menu()
user_entry = input("selecione uma opção de 1 a 6\n")

while user_entry != "6":
    
    try:
        key_func = int(user_entry)-1
        opts[key_func]()
    except ValueError:
        print("Valor inválido, selecione um número de 1 a 6")
    menu()
    user_entry = input("selecione uma opção de 1 a 6\n")

print("programa encerrado")