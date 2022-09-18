import unittest
from graph import Graph
from collections import defaultdict

class GraphTest(unittest.TestCase):

    
    def test_add_node(self):
        G = Graph()
        G.add_node("João")
        self.assertEqual(G.list['João'], [], msg="Verifica se João foi inicializado")
        self.assertTrue(G.add_node("Luiz"), msg="Verifica se Luiz foi adicionado")
        self.assertFalse(G.add_node("Luiz"), msg="Verifica se Luiz não foi adicionado após ser adicionado")


    def test_add_edge(self):
        G = Graph()
        G.add_node("Test2")
        G.add_edge(u="João", v="Test2", weight=3)
        
        self.assertEqual(G.list['João'], [("Test2", 3)], "Verifica se João recebeu a aresta Teste2 com peso 3")
        G.add_node("Test3")
        G.add_edge(u="João", v="Test3", weight=4)
        self.assertEqual(G.list['João'], [("Test2", 3), ("Test3", 4)], msg="Verifica se foi adicionado a aresta Test3 com peso 4")
        G.add_edge(u="João", v="Test4", weight=5)
        self.assertEqual(G.list['João'], [("Test2", 3), ("Test3", 4)], msg="Verifica se João não recebeu vértice não inicializado")

    def test_remove_edge(self):
        G = Graph()
        G.add_node(u="Maria")
        G.add_edge(u="Pedro", v="Maria", weight=3)
        
        G.remove_edge(u="Pedro", v="Maria")
        self.assertEqual(G.list["Pedro"], [], msg="removeu Maria do vértice Pedro")

        G.add_node("Test2")
        G.add_node("Test3")
        G.add_edge(u="Pedro", v="Test2", weight=6)
        G.add_edge(u="Pedro", v="Test3", weight=3)
        G.remove_edge(u="Pedro", v="Test3")
        self.assertEqual(G.list["Pedro"], [("Test2", 6)], msg="Verifica se a vértice com Maria foi removida")

    def test_remove_node(self):
        G = Graph()
        G.add_node("test")
        G.remove_node("test")
        self.assertEqual(G.list, defaultdict(list), "Verifica se a lista está vazia após remover o vértice test")
        G.add_node("test")
        G.add_node("test1")
        G.add_node("test2")
        G.add_edge(u="test4", v="test1", weight=4)
        G.add_edge(u="test4", v="test", weight=2)
        G.remove_node("test")
        self.assertNotIn("test", G.list, msg="Verifica se vértice test1 foi removido do grafo")
        self.assertEqual(G.list["test4"], [("test1", 4)], msg="Verifica se a aresta com o test não foi removido do vértice test4 e se test foi removido")
    def test_check_edge(self):
        G = Graph()
        G.add_node("test1")
        G.add_edge(u="test4", v="test1", weight=4)

        self.assertTrue(G.check_edge(u="test4", v="test1"), msg="Verifica se retornou positivo na aresta test1 do vértice test4")
        self.assertFalse(G.check_edge(u="test4", v="test2"), msg="Verifica se deu falso na inexistência da aresta com test2")

    def test_degree(self):
        G = Graph()
        G.add_node("test1")
        G.add_node("test2")
        G.add_edge(u="test", v="test1", weight=14)
        G.add_edge(u="test", v="test2", weight=4)
        self.assertEqual(G.degree("test"), 2, msg="verifica se contabilizou corretamente o grau de saída")
        G.add_edge(u="test2", v="test", weight=4)
        G.add_edge(u="test1", v="test", weight=4)
        self.assertEqual(G.degree("test"), 4, msg="Verifica se contabilizou corretamente o grau de entrada")

    def test_weight(self):
        G = Graph()
        G.add_node("test1")
        G.add_edge(u="test", v="test1", weight=14)

        self.assertEqual(G.weight("test", "test1"), 14, msg="Verifica se o pegou o peso corretamente")
        self.assertEqual(G.weight("test", "test2"), None, "Verifica se retorna none para vértices inexistentes")

    def test_print_list_adj(self):
        G = Graph()
        G.add_node("test1")
        G.add_node("test2")
        G.add_edge(u="test", v="test1", weight=14)
        G.add_edge(u="test", v="test2", weight=3)
        G.add_edge(u="test1", v="test2", weight=4)
        G.print_list_adj()

if __name__ == '__main__':
    unittest.main()