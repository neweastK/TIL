from pprint import pprint
arr = [[0]*10 for _ in range(10)]

for _ in range(4) :
    loc = list(map(int,input().split()))
    j1 = loc[0]
    i1 = loc[1]
    j2 = loc[2]
    i2 = loc[3]
    for j in range(j1,j2):
        for i in range(i1,i2):
            arr[i][j] = 1

total = 0
for a in arr :
    total += sum(a)

pprint(arr)