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

    def degree(self, u):
        count = 0
        for i in self.list:
            if self.check_edge(i, u):
                count += 1
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
