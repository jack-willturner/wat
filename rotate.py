def rotate(m):
    N = len(m)
    r = [[0]*N for i in range(N)] # <- this works 
    r = [[0]*N]*N                 # <- this doesn't work
    
    for i, j in zip(range(N), range(N-1, -1, -1)):
        for k in range(N):  
            r[k][i] = m[j][k] 
    return r

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(m)
print(rotate(m))
