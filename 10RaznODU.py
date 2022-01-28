import numpy as np

########################################################################################################################

V = T = 1
n = 10
h = T / n

y0 = 0
yn = 0

########################################################################################################################
def X(n, h):
    x = np.zeros(n+1)
    #x[0] = 0.1
    for i in range (1, n+1):
        x[i] = x[i-1] + h
    print(x)
    return x

def P(x):
    return x * x

def Q(x):
    return x

def Ycorrect(x, V, T):
    return V * x * x * (x - T)

def F(x, V, T):
    return 4 * V * (x ** 4) - 3 * V * (x ** 3) + 6 * V * x - 2 * V * T

def boundaryODU(h,q,p,f,y0,yn):
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
    print(yres)
    return yres

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

fk = np.zeros(len(x))
for i in range(len(x)):
    fk[i] = F(x[i], V, T)

y = boundaryODU(h,qk,pk,fk, y0, yn)
a = correctSolution(n, x, V, T)
e = error(y, a)