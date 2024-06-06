# Operações de matrizes

# Importar biblioteca numpy
import numpy as np

# Construção de matrizes:
matriz_1 = np.array([
    [1,3,23,5],
    [54,76,90,20],
    [32,6,4,76],
    [1,2,3,4]
])
print("Matriz 1:")
print(matriz_1)
print('\n')

print("Matriz 2:")
matriz_2 = np.arange(1,17).reshape(4,4)
print(matriz_2)
print('\n')


# Construção utilizando vetores (tuplas ou lista)
# Construção por linhas
x = [1, 4, 7]
y = [2, 5, 8]
z = [3, 6, 9]
matriz_3 = np.array([x,y,z])
print('Matriz 3 construída através de vetores organizados por linhas:')
print(matriz_3)
print('\n')


# Construção por colunas
matriz_4 = np.column_stack((x, y, z))
print('Matriz 4 construída através de vetores organizados por colunas:')
print(matriz_4)
print('\n')


# Manipulação de elementos (substituição de elementos)
# Alterando um elemento (linha 2, coluna 3)
matriz_1[1, 2] = 100
print("Matriz 1 após alteração de 1 elemento:")
print(matriz_1)
print('\n')

#Alterando vários elementos
matriz_1[matriz_1>20] = 11
print("Matriz 1 após alteração de todos os elementos maiores que 20")
print(matriz_1)
print('\n')


# Operações:
# Soma entre as matrizes matriz1 e Matriz2
matriz_5 = matriz_1 + matriz_2
print('Matriz 5 (soma das matrizes 1 e 2)')
print(matriz_5)
print('\n')

# Subtração entre os elementos das matrizes: matriz1 - Matriz2
matriz_6 = matriz_1 - matriz_2
print('Matriz 6 (subtração das matrizes 1 e 2)')
print(matriz_6)
print('\n')

# Multiplicação entre os elementos das matrizes: matriz1 * Matriz2
matriz_7 = matriz_3.dot(matriz_4)
print('Matriz 7 (multiplicação entre as matrizes 3 e 4)')
print(matriz_7)
print('\n')

# Multiplicação por escalar de matriz 2:
matriz_8 = matriz_2 * 2
print('Matriz 8 (multiplicação por escalar com a matriz 2)')
print(matriz_8)
print('\n')


# Determinante
determinante = np.linalg.det(matriz_1)
print('Determinante da matriz 1')
print(determinante)
print('\n')


# Dimensão
dimensao = matriz_1.shape
print('Dimensões da matriz 1')
print(dimensao)
print('\n')


# Extração da diagonal
diagonal = np.diagonal(matriz_2)
print('Valores da diagonal da matriz 2')
print(diagonal)
print('\n')


# Manipulação dos valores da diagonal
print('Troca dos valores da diagonal da matriz 2 por 0')
np.fill_diagonal(matriz_2,0)
print(matriz_2)
print('\n')



# Juntar matrizes
# Por linhas
matriz_9 = np.vstack((matriz_1,matriz_2))
print('Junção das matrizes 1 e 2 por linhas')
print(matriz_9)
print('\n')

# Por colunas
matriz_10 = np.hstack((matriz_1,matriz_2))
print('Junção das matrizes 1 e 2 por colunas')
print(matriz_10)