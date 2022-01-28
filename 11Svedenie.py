import numpy as np

########################################################################################################################

V = T = 1
n = 10
h = T / n

y0 = 1
yn = V + 1

zd1 = (yn - y0) / T
zd2 = 0

########################################################################################################################
def X(n, h):
    x = np.zeros(n+1)
    for i in range (1, n+1):
        x[i] = x[i-1] + h
    print(x)
    return x

def P(x):
    return x * x

def Q(x):
    return x

def Ycorrect(x, V, T):
    return V * x * x * x + 1

def Z(x, a, b, T):
    return (b - a) * x / T + a

def F(x, V, T):
    return 4 * V * (x ** 4) - x * (6 * V + 1)

def rightPart(f, p, q, zd2, zd1, z):
    rp = np.zeros(len(f))
    for i in range (len(f)):
        rp[i] = f[i] - zd2 - p[i] * zd1 - q[i] * z[i]
    return rp

def result(y0, z):
    for i in range (len(y0)):
        y0[i] += z[i]
    print(y0)
    return y0

def svedenie(h,q,p,f,y0,yn, z):
    A = np.zeros((n-1,n-1))
    B = np.zeros(n-1)

    for i in range(0,n-1):
        if(i!=0):
            A[i,i-1] = 1/(h*h)-p[i+1]/(2*h)
        A[i,i] = -2/(h*h) + q[i+1]
        if (i!=n-2):
            A[i,i+1] = 1/(h*h)+p[i+1]/(2*h)
        B[i] = f[i+1]

    y = np.linalg.solve(A,B)
    yres = [y0]
    for i in range (len(y)):
        yres.append(y[i])
    yres.append(yn)

    return result(yres, z)

def correctSolution(n, x, V, T):
    a = np.zeros(len(x))
    for i in range(len(x)):
        a[i] = Ycorrect(x[i], V, T)
    print(a)
    return a

def error(y, a):
    e = np.zeros(len(y))
    for i in range(len(y)):
        e[i] = y[i] - a[i]
    print(e)
    return e

########################################################################################################################

x = X(n, h)

pk = np.zeros(len(x))
for i in range(len(x)):
    pk[i] = P(x[i])

qk = np.zeros(len(x))
for i in range(len(x)):
    qk[i] = Q(x[i])

zk = np.zeros(len(x))
for i in range(len(x)):
    zk[i] = Z(x[i], y0, yn, T)
zk[0] = y0
zk[len(zk)-1] = yn

fk = np.zeros(len(x))
for i in range(len(x)):
    fk[i] = F(x[i], V, T)

rpk = rightPart(fk, pk, qk, zd2, zd1, zk)

y = svedenie(h, qk, pk, rpk, 0, 0, zk)
a = correctSolution(n, x, V, T)
e = error(y, a)