from collections import defaultdict
import json
from pprint import pprint
from numpy import inf

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
        return len(self.graph[u])
    

    def weight(self, u, v):
        for i in self.graph[u]:
            if i[0] == v:
                return i[1]
        return None

    def print_graph_adj(self):
        line = ""
        file = open("output_graph.txt", "w")
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
    
    def dijkstra(self, u, all_nodes=False): 
        if all_nodes:
            if len(self.graph[u]) == 0:
                return {}
        inf = float("inf")
        cost = {key: [inf, ""] for key in self.graph }
        cost[u] = [0,"-"]
        visited = {key: False for key in self.graph}
        current_node = u
        while not visited[current_node]:
            adjacent_nodes = self.graph[current_node]
            for k,v in adjacent_nodes:

                if visited.get(k) == None:
                    cost[k] = [inf,""] 
                    visited[k] = False
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
        return cost

    def djijkstra_min_path(self, v, cost):
        path=[v]
        current_node = v
        while cost[current_node][1] != "-":
            
            current_node = cost[current_node][1]
            path.append(current_node)
        path.reverse()
        return cost[v][0],path

    def min_max_path(self, u):
        cost = self.dijkstra(u)
        max_node =[ float("-inf"), "-"]
        inf = float("inf")
        for k in cost:
            if cost[k][0] > max_node[0] and cost[k][0]!=inf:
                max_node = [cost[k][0], k]
        print(max_node)
        path = self.djijkstra_min_path(max_node[1], cost)
        return max_node, path

    def dijkstra_warshall(self, u, desired_weight): # percorre o grafo a partir do node u e retorna o peso do caminho até cada node
        inf = float("inf")
        cost = {key: [inf, ""] for key in self.graph }
        cost[u] = [0,"-"]
        visited = {key: False for key in self.graph}
        desired_distance = []
        current_node = u
        while not visited[current_node]:
            adjacent_nodes = self.graph[current_node]
            # if visited[current_node]:
            #     return path,cost
            for k,_ in adjacent_nodes:
                if visited.get(k) == None: 
                    visited[k] = True
                if not  visited[k]:
                    new_dist = cost[current_node][0] + 1
                    if new_dist < cost[k][0]:
                        cost[k][0] = new_dist
                        cost[k][1] = current_node
            visited[current_node]=True
            # if cost[current_node][0] == desired_weight:
            #     path.append(current_node)
            min_value = inf
            min_node = ""
            for key in cost:
                if visited.get(key) == None: 
                    visited[key] = True
                if visited[key]:
                    continue
                if min_value >= cost[key][0]:
                    min_value=cost[key][0]
                    min_node = key
            if min_node=="":
                break
            current_node=min_node
        
        for k in cost:
            if cost[k][0]==desired_weight:
                desired_distance.append(k)
        return desired_distance

    def Dijkstra(self, origem, alvo):
        import numpy as np
        
        visitados = []
        ListaCustoAnterior = {}
        visitaveis = []
        for vertice in self.graph.keys():
            if (self.exitDegree(vertice) == 0 or self.entryDegree(vertice) == 0) and vertice != alvo and vertice != origem:
                continue
            elif vertice == origem:
                ListaCustoAnterior[vertice] = [vertice, 0]
                visitaveis.append(vertice)
            else:
                ListaCustoAnterior[vertice] = [vertice, np.inf]
                visitaveis.append(vertice)
        nodeAtual = origem
        while len(visitados) < len(visitaveis):
            # Obtém os nós adjacentes do nó atual
            adjacent_nodes = self.graph[nodeAtual]
            # Itera por cada nó adjacente
            for adj in adjacent_nodes:
                if adj in visitaveis and adj not in visitados:
                    # Caso o nó ainda não tenha sido visitado, verifica o caminho
                    # if adj not in visitados:
                    # Obtém o peso da distância do nó de origem até o nó adjacente
                    acc_cost = ListaCustoAnterior.get(nodeAtual)[1] + self.graph.get(nodeAtual).get(adj)
                    # Se o peso é menor que o peso nele registrado, registra o novo peso e o nó de origem
                    if ListaCustoAnterior.get(adj)[1] > acc_cost:
                        ListaCustoAnterior.get(adj)[1] = acc_cost
                        ListaCustoAnterior.get(adj)[0] = nodeAtual
            # Iteração concluída, adiciona o Nó à lista de visitados
            visitados.append(nodeAtual)
            # Separação dos nós visitados dos não visitados
            non_visted = [item for item in visitaveis if item not in visitados]
            if non_visted != []:
                # Busca pelo nó não visitado com o menor peso acumulado
                nodeAtual = non_visted[0]
                for vertice in non_visted:
                    if ListaCustoAnterior.get(vertice)[1] < ListaCustoAnterior.get(nodeAtual)[1]:
                        nodeAtual = vertice
        # Processo para encontrar o caminho
        
        caminho = [alvo]
        custo = ListaCustoAnterior.get(alvo)[1]
        contador = 0
        # Busca inicia a partir do destino, e vai retornando pelos caminhos mais leves até a origem
        passo = ListaCustoAnterior.get(alvo)[0]
        while contador < len(visitaveis):
            caminho.insert(0, passo)
            if passo == origem:
                return caminho, custo
            passo = ListaCustoAnterior.get(passo)[0]
            contador += 1

    

    def graph_diameter(self):
        cost_scan = {}
        with open("outputs/dijkstra_scan.json", "r") as file:
            cost_scan=json.loads(file.read())

        counter =0
        max_node=[float("-inf"),"-"]
        remote_node = ""
        init_remote_node = ""
        max_cost = {}
        for node in cost_scan:
            for edge in cost_scan[node]:
                
                if cost_scan[node][edge][0] != float("inf") and cost_scan[node][edge][0] > max_node[0]:
                    max_node = cost_scan[node][edge]
                    remote_node=edge
                    init_remote_node=node
                    max_cost=cost_scan[node]
                
        print(f"{init_remote_node} {remote_node}")
        print(self.djijkstra_min_path(remote_node, max_cost))
        print(max_node)

    def scan_graph_with_dijkstra(self):
        counter =0
        n_nodes = self.n_nodes()
        inf = float("inf")
        dijkstras_costs = {}
        for node in self.graph:
            print(f"\r{counter}/{n_nodes}", sep="", end="")
            counter+=1
            cost = self.dijkstra(node, all_nodes=True)
            if cost != {}:
        
                dijkstras_costs[node]=cost
            
            
        
        with open("outputs/dijkstra_scan.json", "w") as file:
            file.write(json.dumps(dijkstras_costs))
        

    def BFS(self, v, u):
        queue = []
        queue.append(v)
        visited = {key: False for key in self.graph}
        path = []
        while len(queue)>0:
            n = queue.pop(0)
            if n not in visited: visited[n]=True
            if not visited[n]:
                 visited[n] = True
                 path.append(n)
            if(n==u): return True,path
            adj = self.graph[n]
            for vertice in adj:
                # if vertice[0] not in visited:
                if visited.get(vertice[0]) == None: 
                    visited[vertice[0]] = True
                if not visited[vertice[0]]:
                    queue.append(vertice[0])
        return False,path

    # def BFS(self, v, u):
    #     fila = []
    #     fila.append(v)
    #     visitados = []
    #     while len(fila)>0:
    #         n = fila.pop(0)
    #         if n not in visitados: visitados.append(n)
    #         if(n==u): return True, visitados
    #         adj = self.graph[n]
    #         for vertice in adj:
    #             if vertice[0] not in visitados:
    #                 fila.append(vertice[0])
    #     return False, visitados
        
    # def DFS(self,v,u):
    #     pilha = []
    #     pilha.append(v)
    #     visitados = []
    #     while pilha!=[]:
    #         n = pilha.pop()
    #         if n not in visitados: visitados.append(n)
    #         if(n==u): return True,visitados
    #         adj = self.graph[n]
    #         for vertice in adj:
    #             if vertice[0] not in visitados:
    #                 pilha.append(vertice[0])
    #     return False, visitados
        
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
            if(n==u): return True, path
            adj = self.graph[n]
            for vertice in adj:
                if visited.get(vertice[0]) == None: 
                    visited[vertice[0]] = True 
                if not visited[vertice[0]]:
                    stack.append(vertice[0])
        return False, path      


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
 



if __name__ == "__main__":
    main()