
def floyd_warshall(A):
    """
    A is the matrix of distances between nodes.
    """
    n,m = A.shape
    I = np.identity(n)
    A[I == 1] = 0 # diagonal elements should be zero
    for i in range(n):
        A = np.minimum(A, A[i,:] + A[:,i])
