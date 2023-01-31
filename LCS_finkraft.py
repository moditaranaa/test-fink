

def longestCommonSubs(X,Y):
    if len(X)>len(Y):
        t=X
        X=Y
        y=t
    
    n=len(X)
    m=len(Y)
    dp = [[0 for i in range(m+1)] for j in range (n+1)]

    longest=0
    lcss = []
    for i in range(n):
        for j in range(m):
            if X[i]==Y[j]:
                c = dp[i][j]+1
                dp[i+1][j+1]=c
                if c>longest:
                    longest = c
                    lcs = X[i-c+1:i+1]


    return lcs


print(longestCommonSubs('ABCFD','ABCFGFDGDGDF'))