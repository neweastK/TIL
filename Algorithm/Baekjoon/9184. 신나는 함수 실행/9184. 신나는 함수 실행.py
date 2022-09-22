import sys
input = sys.stdin.readline

maps = [[[0]*21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i==0 or j==0 or k==0 :
                maps[i][j][k] = 1
            elif i<j<k :
                maps[i][j][k] = maps[i][j][k-1]+maps[i][j-1][k-1]-maps[i][j-1][k]
            else :
                maps[i][j][k] = maps[i-1][j][k]+maps[i-1][j-1][k]+maps[i-1][j][k-1] - maps[i-1][j-1][k-1]

while True :
    a,b,c = map(int,input().split())
    if (a,b,c) == (-1,-1,-1) :
        break
    elif a<=0 or b<=0 or c<=0 :
        res = maps[0][0][0]
    elif a>20 or b>20 or c>20 :
        res = maps[20][20][20]
    else :
        res = maps[a][b][c]
    print(f"w{a,b,c} = {res}")