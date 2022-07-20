import sys
input = sys.stdin.readline

N,M = map(int,input().split())

a = set()
b = set()
for _ in range(N):
    name = input().rstrip()
    a.add(name)

for _ in range(M):
    name2 = input().rstrip()
    b.add(name2)

res = list(a&b)
print(len(res))
for i in sorted(res) :
    print(i)


