from collections import defaultdict
from pprint import pprint
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
        return len(self.graph[u])

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
                line+=f"({j[0]} {j[1]} )-> "
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
        for i in self.graph:
            nodes.append((self.exitDegree(i),i))
        nodes.sort(reverse=True)
        return nodes[:20]

    def maior20entrada(self): # retorna os 20 nodes com o maior grau de entrada e o valor
        nodes = []
        for i in self.graph:
            nodes.append((self.entryDegree(i),i))
        nodes.sort(reverse=True)
        return nodes[:20]

    def is_euleriano(self): # verifica se o grafo é Euleriano (possui um ciclo contendo todas os nodes)
        in1out = False
        out1in = False
        for i in self.graph:
            if (in1out == False) and (self.entryDegree(i)+1 == self.exitDegree(i)):
                in1out = True
            if (out1in == False) and (self.entryDegree(i) == self.exitDegree(i)+1):
                out1in = True
            if (self.entryDegree(i) == 0) or (self.exitDegree(i) == 0) or (self.entryDegree(i) != self.exitDegree(i)):
                return False
        if (in1out == False) or (out1in == False):
            return False
        return True
    
    def dijkstra(self, u): # percorre o grafo a partir do node u e retorna o peso do caminho até cada node
        cost = {key: [inf, ""] for key in self.list }
        cost[u] = [0,"-"]
        visited = {key: False for key in self.list}
        current_node = u
        while True:
            adjacent_nodes = self.list[current_node]
            if visited[current_node]:
                return cost
            if len(adjacent_nodes)==0:
                visited[current_node]=True
            for k,v in adjacent_nodes:
                if not  visited[k]:
                    new_dist = cost[current_node][0] + v
                    if new_dist < cost[k][0]:
                        cost[k][0] = new_dist
                        cost[k][1] = current_node
            visited[current_node]=True
            min_value = inf
            min_node = ""
            for key in cost:
                if visited[key]:
                    continue
                if min_value >= cost[key][0]:
                    min_value=cost[key][0]
                    min_node = key
            if min_node=="":
                break
            current_node=min_node
        print("djikstra end")
        return cost

    def great_min_path(self, source_node, destinity_node):
        return self.dijkstra(source_node)[destinity_node]


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
    print(grafo1.dijkstra("B"))


if __name__ == "__main__":
    main()