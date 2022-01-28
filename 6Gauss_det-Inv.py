import numpy as np

########################################################################################################################

A = np.array([
    [ 2.0, 1.0,   0.0, 0.0 ],
    [ 1.0, 10.0, -5.0, 0.0 ],
    [ 0.0, 1.0,  -5.0, 2.0 ],
    [ 0.0, 1.0,   1.0, 4.0 ]
])

B = [
    -5.0,
    -18.0,
    -40.0,
    -27.0
]

print("Matrix A:")
print(A)

print("B:")
print(B)
print()

jmx = 0

########################################################################################################################

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
    ++jmx

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

    # обратный ход
    for k in range(n-1, -1, -1):
        d = 0
        for j in range(k+1, n):
            s = A[k][j] * x[j]
            d = d + s
        x[k] = (B[k] - d) / A[k][k]

    return x

########################################################################################################################

def GaussDet(A, B, n):
    det = 1

    # прямой ход
    for k in range(0, n):
        for j in range(k+1, n):
            if A[k][k] == 0:
                swap(k, k, n, A)
            d = A[j][k] / A[k][k]
            for i in range(k, n):
                A[j][i] = A[j][i] - d * A[k][i]
            B[j] = B[j] - d * B[k]

    for i in range (0, n):
        det *= A[i][i]

    jx = 1 if jmx % 2 == 0 else -1
    return det * jx

def reversMx(mx, n):
    res = np.zeros((n,n))
    for i in range(0, n):
        for j in range (0, n):
            res[j][i] = mx[i][j]
    return res


def invMatrix (A, n):
    invRev = np.zeros((n,n))
    for i in range (0, n):
        A0 = A
        ze = np.zeros(n)
        ze[i] = 1
        Xk = np.linalg.solve(A, ze) #коэфф-ы а
        for j in range (0, n):
            invRev[i] = Xk
    return reversMx(invRev, n)

########################################################################################################################

A0 = np.array(A)

detMx = GaussDet(A, B, len(B))
print("Determinant:")
print(detMx)
print()

print("Inverse NUMPY matrix:")
invMxnp = np.linalg.inv(A0)
print(invMxnp)

invMx = invMatrix(A0, len(B))
print("Inverse matrix:")
print(invMx)
