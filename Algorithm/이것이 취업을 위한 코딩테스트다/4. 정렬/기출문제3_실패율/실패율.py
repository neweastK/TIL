'''
4
5 1 7 9
'''

N = int(input())
houses = list(map(int,input().split()))

houses.sort()
antena1 = houses[N//2]
antena2 = houses[N//2-1]
sum1 = 0
sum2 = 0
for house in houses :
    sum1 += abs(antena1 - house)
    sum2 += abs(antena2 - house)

if sum1 >= sum2 :
    print(antena2)
else :
    print(antena1)
