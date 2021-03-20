import numpy as np
import matplotlib.pyplot as plt


# Creamos matriz A
A = [
    [1, 2],
    [4, 5],
    [7, 8]
]
B = [
    [3, 6, 9],
    [3, 6, 9]
]

# Convertimos a array de numpy
A = np.array(A)
B = np.array(B)



def multiplica_matriz(A, B):

    a_rows, a_cols = A.shape
    b_rows, b_cols = B.shape

    if b_rows != a_cols:
        print("Las dimensiones no corresponden.")
        return -1

    # Matriz resultante
    M = np.zeros((a_rows, b_cols))

    for i in range(b_cols):
        for j in range(a_rows):
            M[j, i] = np.sum(B[:, i] * A[j, :])

    return M

M = multiplica_matriz(A, B)
print(M)