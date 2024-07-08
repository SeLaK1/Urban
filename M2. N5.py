from random import *
def get_matrix(n, m, value):
    matrix = [['']*n]*m
    for i in range(n):
        for j in range(m):
            matrix[i][j] = value
    return matrix

print(get_matrix(4,4, randint(1, 50)))