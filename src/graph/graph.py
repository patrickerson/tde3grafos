from collections import defaultdict

class Graph:

    def __init__(self):
        self.list = defaultdict(list)

    def add_node(self, u):
        if u not in self.list:
            self.list[u] = []
            return True
        else:
            return False

    def add_edge(self, u, v, weight=0):
        self.add_node(u)
        if v not in self.list:
            return False
        self.list[u].append((v, weight))
        return True

    def remove_edge(self, u, v):
        for edge in self.list[u]:
            if edge[0] == v:
                self.list[u].remove(edge)

    def remove_node(self, u):
        for k in self.list:
            if self.check_edge(k,u):
                self.remove_edge(k,u)
        self.list.pop(u)

    def check_edge(self, u, v):
        for i in self.list[u]:
            if i[0] == v:
                return True
        return False

    def entryDegree(self, u):
        count = 0
        for i in self.list:
            if self.check_edge(i, u):
                count += 1
        return count

    def exitDegree(self, u):
        count = 0
        for i in self.list:
            if self.check_edge(u, i):
                count += 1
        return count

    def weight(self, u, v):
        for i in self.list[u]:
            if i[0] == v:
                return i[1]
        return None

    def print_list_adj(self):
        line = ""
        print(self.list)
        print("------------")
        for i in self.list:
            line+=f"{i} -> "
            for j in self.list[i]:
                line+=f"{j} -> "
            print(line)
            line=""

    def n_nodes(self): # retorna número de vértices do grafo
        return len((self.list))
    
    def n_edge(self): # retorna número de arestas do grafo
        count = 0
        for i in self.list:
            count += len(self.list[i])
        return count

    def maior20saida(self): # retorna os 20 nodes com o maior grau de saida e o valor
        nodes = []
        
        return nodes # [(node, grauDeSaida),...]

    def maior20entrada(self): # retorna os 20 nodes com o maior grau de entrada e o valor
        nodes = []

        return nodes # [(node, grauDeEntrada),...]

    def is_Euleriano(self): # verifica se o grafo é Euleriano (possui um ciclo contendo todas os nodes)
        if 0 == 0:
            return True
        return False

    def profundo(self, u, v): # recebe dois nodes
        # realiza uma busca em profundidade
        return u, v # retorna lista de visitados + tempo
    
    def largo(self, u, v): # recebe dois nodes
        # realiza uma busca em largura
        return u, v # retorna lista de visitados + tempo

    def distancia(self, u, v): # recebe um node e a distancia
        return u, v # retorna [nodes a uma distancia v de u]
    
    def dijkstra(self, u): # percorre o grafo a partir do node u e retorna o peso do caminho até cada node
        return u # [(node, peso minimo),...]