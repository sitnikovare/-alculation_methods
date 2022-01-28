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

commonMx = np.array([
    [ 2.0, 1.0,   0.0, 0.0, -5.0 ],
    [ 1.0, 10.0, -5.0, 0.0, -18.0 ],
    [ 0.0, 1.0,  -5.0, 2.0, -40.0 ],
    [ 0.0, 1.0,   1.0, 4.0, -27.0 ]
])

eps = 0.01

########################################################################################################################

def simpleIteration (commonMx, size):
    prevVar = np.zeros(size)
    countIter = 0
    while (True):
        countIter += 1
        curVar = np.zeros(size)
        for i in range (size):
            curVar[i] = commonMx[i][size]
            for j in range (size):
                if i != j:
                    curVar[i] -= commonMx[i][j] * prevVar[j]
            curVar[i] /= commonMx[i][i]

        err = 0.0
        for i in range (size):
            err += abs(curVar[i] - prevVar[i])
        if err < eps:
            break
        prevVar = curVar
    print("Количество итераций: " + str(countIter))
    return prevVar

########################################################################################################################

print("Solution:")
x = simpleIteration(commonMx, len(A))
print(x)

print()
print("Check:")
x0 = np.linalg.solve(A, B)
print(x0)
