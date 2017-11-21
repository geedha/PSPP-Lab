def matrixmulti(X, Y):
    M = len(X)
    N = len(X[0])
    P = len(Y[0])
    Z = [[0] * P  for row in range(M)]
    
    if  N != len(Y):  
        print ("Incorrect dimensions.")
        return

    for i in range(M):
        for j in range(P):
            for k in range(N):
                Z[i][j] += X[i][k] * Y[k][j]

    return Z

X = [[2,3],[4,5],[6,7]]
Y = [[1,2,3],[4,5,6]]
print(matrixmulti(X,Y))
