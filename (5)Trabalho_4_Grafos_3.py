import networkx as nx
import trabalho_3_grafo_2 as tr3
# Criando um grafo
G1 = nx.Graph(tr3.g_coo)
#G1.add_nodes_from(['v1', 'v2', 'v3', 'v4', 'v5'])
#G1.add_edges_from([('v1', 'v2'), ('v2', 'v3'), ('v3', 'v4'), ('v4', 'v5'), ('v5', 'v1')])
print('Grafo 1')
# Identificando os vértices
vertices = list(G1.nodes)
print("Vértices:", vertices)

# Contagem do número de vértices
num_vertices = G1.number_of_nodes()
print("Número de vértices:", num_vertices)

# Identificando as Arestas
ligacoes = list(G1.edges)
print("Ligações:", ligacoes)

# Contagem do número de arestas
num_arestas = G1.number_of_edges()
print("Número de arestas:", num_arestas)

# Graus dos vértices
graus = G1.degree()
print("Graus dos vértices:", graus)

# Grau médio
grau_medio = sum(dict(graus).values()) / num_vertices
print("Grau médio:", grau_medio)

# Pesos do grafo (nesse exemplo, não há pesos)
pesos = nx.get_edge_attributes(G1, 'weight')
print("Pesos do grafo:", pesos)

# Força de conectividade média
forca_conectividade = nx.average_degree_connectivity(G1)
print("Força de conectividade média:", forca_conectividade)

# Densidade
densidade = nx.density(G1)
print("Densidade:", densidade)

print('________________________________________')
print('\n')
#Grafo Similaridade
G2= nx.Graph(tr3.g_sim)
print('Grafo 2:')
# Identificando os vértices
vertices = list(G2.nodes)
print("Vértices:", vertices)

# Contagem do número de vértices
num_vertices = G2.number_of_nodes()
print("Número de vértices:", num_vertices)

# Identificando as Arestas
ligacoes = list(G2.edges)
print("Ligações:", ligacoes)

# Contagem do número de arestas
num_arestas = G2.number_of_edges()
print("Número de arestas:", num_arestas)

# Graus dos vértices
graus = G2.degree()
print("Graus dos vértices:", graus)

# Grau médio
grau_medio = sum(dict(graus).values()) / num_vertices
print("Grau médio:", grau_medio)

# Pesos do grafo (nesse exemplo, não há pesos)
pesos = nx.get_edge_attributes(G2, 'weight')
print("Pesos do grafo:", pesos)

# Força de conectividade média
forca_conectividade = nx.average_degree_connectivity(G2)
print("Força de conectividade média:", forca_conectividade)

# Densidade
densidade = nx.density(G2)
print("Densidade:", densidade)
