from collections import defaultdict
from pprint import pprint

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def increment_edge(self, u, v):
        for i in self.graph[u]:
            if i[0] == v:
                i[1]+=1
                return True
        self.add_edge(u,v,1)
        return False

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = []
            return True
        else:
            return False

    def add_edge(self, u, v, weight=0):
        self.add_node(u)
        if v not in self.graph:
            return False
        self.graph[u].append([v, weight])
        return True

    def remove_edge(self, u, v):
        for edge in self.graph[u]:
            if edge[0] == v:
                self.graph[u].remove(edge)

    def remove_node(self, u):
        for k in self.graph:
            if self.check_edge(k,u):
                self.remove_edge(k,u)
        self.graph.pop(u)

    def check_edge(self, u, v):
        for i in self.graph[u]:
            if i[0] == v:
                return True
        return False

    def entryDegree(self, u):
        count = 0
        for i in self.graph:
            if self.check_edge(i, u):
                count += 1
        return count

    def exitDegree(self, u):
        count = 0
        for i in self.graph:
            if self.check_edge(u, i):
                count += 1
        return count

    def weight(self, u, v):
        for i in self.graph[u]:
            if i[0] == v:
                return i[1]
        return None

    def print_graph_adj(self):
        line = ""
        file = open("test.txt", "w")
        for i in self.graph:
            line+=f"{i} -> "
            for j in self.graph[i]:
                line+=f"({j[0]} {j[1]} )-> "
            file.write(f"{line}\n")
            
            line=""
        file.close()
    def n_nodes(self): # retorna número de vértices do grafo
        return len((self.graph))
    
    def n_edge(self): # retorna número de arestas do grafo
        count = 0
        for i in self.graph:
            count += len(self.graph[i])
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
        return u, v # retorna gaph de visitados + tempo
    
    def largo(self, u, v): # recebe dois nodes
        
        for adj in self.graph[u]:
            
            pass
        return u, v # retorna gaph de visitados + tempo

    def distancia(self, u, v): # recebe um node e a distancia
        return u, v # retorna [nodes a uma distancia v de u]
    
    def dijkstra(self, u): # percorre o grafo a partir do node u e retorna o peso do caminho até cada node
        inf = float("inf")
        cost = {key: [inf, ""] for key in self.graph }
        cost[u] = [0,"-"]
        visited = {key: False for key in self.graph}
        path = []
        current_node = u
        while True:
            adjacent_nodes = self.graph[current_node]
            if visited[current_node]:
                return cost
            for k,v in adjacent_nodes:
                if not  visited[k]:
                    new_dist = cost[current_node][0] + v
                    if new_dist < cost[k][0]:
                        cost[k][0] = new_dist
                        cost[k][1] = current_node
            visited[current_node]=True
            path.append(current_node)
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
        return path,cost

    def great_min_path(self, source_node, destinity_node):
        return self.dijkstra(source_node)[destinity_node]

    def BFS(self, v, u):
        stack = []
        stack.append(v)
        visited = {key: False for key in self.graph}
        path = []
        while len(stack)>0:
            n = stack.pop(0)
            if n not in visited: visited.append(n)
            if not visited[n]:
                 visited[n] = True
                 path.append(n)
            if(n==u): return visited
            adj = self.graph[n]
            for vertice in adj:
                # if vertice[0] not in visited:
                if not visited[vertice[0]]:
                    stack.append(vertice[0])
        return visited
        

    def DFS(self,v,u):
        stack = []
        stack.append(v)
        visited = {key: False for key in self.graph}
        path = []
        while stack!=[]:
            n = stack.pop()
            if not visited[n]: 
                visited[n]=True
                path.append(n)
            if(n==u): return path
            adj = self.graph[n]
            for vertice in adj:
                if not visited[vertice[0]]:
                    stack.append(vertice[0])
        return visited      


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
    grafo1.DFS("B", "F")



if __name__ == "__main__":
    main()