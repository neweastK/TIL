import sys

K,L = map(int,sys.stdin.readline().split())

lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

min_val = 1
max_val = sum(lines)//L
res = 0

while min_val<=max_val :
    middle = (min_val+max_val)//2
    cnt = 0
    for line in lines :
        cnt += line//middle
    if cnt>=L :
        min_val = middle+1
        res = middle
    else :
        max_val = middle-1

print(res)
