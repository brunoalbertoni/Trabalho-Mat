# -*- coding: utf-8 -*-

"""Trabalho 3 - Grafo 2.ipynb


# Desafio
Grafos 2: Leitura de arquivo externo em formato de matriz (utilizar
mesmo arquivo da aula); gerar matrizes de incidência, similaridade e
coocorrência; gerar respectivos grafos.

Passo a passo

1.Ler o arquivo e obter a matriz

2.Gerar as demais matrizes

    2.1 Transpostar a original

    2.2 Multiplicá-las

3.Plotar em grafos
"""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


"""Leitura do arquivo:"""

arquivo=pd.read_table("C:/Users/bruno/OneDrive - unimar.br/Faculdade/Matemática Linguagem R/mtz_grafos-main/mtz_grafos-main/mtz_exemplo.txt",
                      sep='\t')
arquivo

"""Formatação do dataframe para matriz:"""

rows=[]
for i in range(len(arquivo.index)):
    rows.append(arquivo.iloc[i].values)

data_base=[]
for i in range(len(arquivo.index)):
    data_base.append(rows[i][1:])
dt=pd.DataFrame(data=data_base,columns=(arquivo.columns[i+1] for i in range(len(arquivo.columns)-1)),index=(rows[i][0] for i in range(len(data_base))))


data_base_t=[]
for i in range(len(dt.columns)):
    data_base_t.append(dt.iloc[:,i].values)
dt_t=pd.DataFrame(data=data_base_t,columns=(rows[i][0] for i in range(len(data_base))),index=(arquivo.columns[i+1] for i in range(len(arquivo.columns)-1)))

dt_t

mtz=dt.to_numpy()
sim=np.dot(mtz,mtz.T)

dt_s=pd.DataFrame(data=sim,columns=(rows[i][0] for i in range(len(rows))),index=(rows[i][0] for i in range(len(rows))))

dt_s

coo=np.dot(mtz.T,mtz)

dt_c=pd.DataFrame(data=coo,columns=(arquivo.columns[i+1] for i in range(len(arquivo.columns)-1)),index=(arquivo.columns[i+1] for i in range(len(arquivo.columns)-1)))

dt_c

g_inc=nx.DiGraph()
g_inc.add_nodes_from(dt.index)
g_inc.add_nodes_from(dt.columns)

for i in dt.index:
    for j in dt.columns:
        if dt.loc[i, j]!=0:
            g_inc.add_edge(i, j)

nx.draw(g_inc,nx.bipartite_layout(g_inc,dt.index), with_labels=True, node_size=1000, node_color='red', font_family='Times New Roman',font_weight='bold')
plt.title('Grafo Matriz Incidência',fontweight='bold')


g_sim=nx.from_pandas_adjacency(dt_s)
g_sim.remove_edges_from(nx.selfloop_edges(g_sim))
nx.draw(g_sim,nx.kamada_kawai_layout(g_sim),with_labels=True,node_size=1000,node_color='red',font_family='Times New Roman',font_weight='bold')
plt.title('Grafo Matriz Similaridade',fontweight='bold')


g_coo=nx.from_pandas_adjacency(dt_c)
g_coo.remove_edges_from(nx.selfloop_edges(g_coo))
nx.draw(g_coo,nx.circular_layout(g_coo),with_labels=True,node_size=1000,node_color='red',font_family='Times New Roman',font_weight='bold')
plt.title('Grafo Matriz Coocorrência',fontweight='bold')
