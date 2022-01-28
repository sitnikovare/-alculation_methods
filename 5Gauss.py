import numpy as np

# A = [
#     [ 1.0, 0.0, 0.0],
#     [ 1.0, 0.0, 1.0],
#     [ 1.0, 2.0, 4.0],
# ]
#
# B = [
#     5.0,
#     6.0,
#     9.0
# ]

A = [
    [ 1.0, 0.0,   0.0],
    [ 1.0, 0.0, 1.0 ],
    [ 1.0, 2.0,  4.0 ]
]

B = [
    5.0,
    6.0,
    9.0
]

print("Matrix A:")
for row in A:
    print(*row)
print()

print("B:")
print(B)
print()

def swap(row, col, n, A):
    max = A[row][col]
    maxR = row
    for i in range(col, n):
        if A[i][col] > max:
            max = A[i][col]
            maxR = i
    for j in range(n):
        A[row][j], A[maxR][j] = A[maxR][j], A[row][j]
    B[row], B[maxR] = B[maxR], B[row]

    print("swap:")
    for row in A:
        print(*row)
    print()


def Gauss(A, B, n):
    x = np.zeros(n)

    # прямой ход
    for k in range(0, n):
        for j in range(k+1, n):
            if A[k][k] == 0:
                swap(k, k, n, A)
            d = A[j][k] / A[k][k]
            for i in range(k, n):
                A[j][i] = A[j][i] - d * A[k][i]
            B[j] = B[j] - d * B[k]

    print("Triangle:")
    for row in A:
        print(*row)
    print()

    # обратный ход
    for k in range(n-1, -1, -1):
        d = 0
        for j in range(k+1, n):
            s = A[k][j] * x[j]
            d = d + s
        x[k] = (B[k] - d) / A[k][k]

    return x


A0 = np.array(A)

X = Gauss(A, B, len(B))
print("Solution:")
print(X)

print("Check")
X0 = np.array(X)
print(A0.dot(X0))
