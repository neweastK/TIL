from pprint import pprint
arr = [[0]*100 for _ in range(100)]

for _ in range(4) :
    loc = list(map(int,input().split()))
    loc_1 = loc[:2]
    loc_2 = loc[2:]

