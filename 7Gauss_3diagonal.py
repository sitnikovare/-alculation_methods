import numpy as np

A = np.array([
     [ 10.8000, 0.0475,      0, 0     ],
     [  0.0321, 9.9000, 0.0523, 0     ],
     [       0, 0.0369, 9.0000, 0.0570],
     [       0,      0, 0.0416, 8.1000]
])

B = [
    12.1430,
    13.0897,
    13.6744,
    13.8972
]

print("Matrix A:")
print(A)
print()

print("B:")
print(B)
print()

def progonka(A, B, n):
    X = np.zeros(n)

    # Прямой ход
    P = [0 for k in range(0, n)]
    Q = [0 for k in range(0, n)]

    P[0] = A[0][1] / (-A[0][0])
    Q[0] = ( - B[0]) / (-A[0][0])
    for i in range(1, n - 1):
        P[i] = A[i][i+1] / ( -A[i][i] - A[i][i-1] * P[i-1] )
        Q[i] = ( A[i][i-1] * Q[i-1] - B[i] ) / ( -A[i][i] - A[i][i-1] * P[i-1] )

    P[n-1] = 0
    Q[n-1] = (A[n-1][n-2] * Q[n-2] - B[n-1]) / (-A[n-1][n-1] - A[n-1][n-2] * P[n-2])

    # Обратный ход
    X[n-1] = Q[n-1]
    for i in range(n-1, 0, -1):
        X[i-1] = P[i-1] * X[i] + Q[i-1]

    return X


A0 = np.array(A)

X = progonka(A, B, len(A))
print("Solution:")
print(X)

print("Check")
X0 = np.array(X)
print(A0.dot(X0))