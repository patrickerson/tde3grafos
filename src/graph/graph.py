from collections import defaultdict
from numpy import inf
class Graph:

    def __init__(self):
        self.list = defaultdict(list)

    def increment_edge(self, u, v):
        for i in self.list[u]:
            if i[0] == v:
                i[1]+=1
                return True
        self.add_edge(u,v,1)
        return False

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
        self.list[u].append([v, weight])
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
        file = open("test.txt", "w")
        for i in self.list:
            line+=f"{i} -> "
            for j in self.list[i]:
                line+=f"{j} -> "
            print(line)
            file.write(f"{line}\n")
            
            line=""
        file.close()
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
    
    def dijkstra(self, u, destiny_node): # percorre o grafo a partir do node u e retorna o peso do caminho até cada node
        cost = {key: [inf, ""] for key in self.list if key !=u }
        cost[u] = [0,"-"]
        visited = []
        current_node = u

        while len(visited) < len(self.list.keys()):
            adjacent_nodes = self.list[current_node]
            if len(adjacent_nodes)==0:
                visited.append(current_node)
            for k,v in adjacent_nodes:
                if k not in visited:
                    print(cost[current_node][0])
                    new_dist = cost[current_node][0] + v
                    if new_dist < cost[k][0]:
                        cost[k][0] = new_dist
                        cost[k][1] = current_node
            visited.append(current_node)
            min_value = inf
            min_node = ""
            for key in cost:
                if key in visited:
                    continue
                if min_value >= cost[key][0]:
                    min_value=cost[key][0]
                    min_node = key
            if min_node=="":
                break
            current_node=min_node
            
        return cost[destiny_node][0]



def main():
    grafo1 = Graph()
    grafo1.add_node("A")
    grafo1.add_node("B")
    grafo1.add_node("C")
    grafo1.add_node("D")
    grafo1.add_node("E")
    grafo1.add_node("F")
    grafo1.add_edge("B", "C", 1)
    grafo1.add_edge("B", "A", 4)
    
    grafo1.add_edge("C", "A", 2)
    grafo1.add_edge("C", "E", 10)
    grafo1.add_edge("D", "F", 6)
    grafo1.add_edge("B", "D", 5)
    grafo1.add_edge("E", "F", 2)
    grafo1.add_edge("D", "C", 8)
    grafo1.add_edge("D", "E", 2)
    grafo1.add_edge("C", "D", 8)
    grafo1.print_list_adj()
    print(grafo1.dijkstra("B","E"))


if __name__ == "__main__":
    main()