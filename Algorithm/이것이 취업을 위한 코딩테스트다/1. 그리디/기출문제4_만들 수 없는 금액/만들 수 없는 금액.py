from itertools import combinations

N = int(input())
coins = list(map(int,input().split()))


total = []
for i in range(1,len(coins)+1) :

    combis = combinations(coins,i)

    for combi in combis :
        total.append(sum(combi))

standard = 1
loc=0
while True :
    if standard in total :
        standard +=1

    else :
        ans = standard
        break
print(ans)
