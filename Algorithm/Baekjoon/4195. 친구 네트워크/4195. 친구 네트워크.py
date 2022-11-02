import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)

    if a>b:
        parent[a] = b
        number[b] += number[a]
        return b
    else:
        parent[b] = a
        number[a] += number[b]
        return a

T = int(input())

for _ in range(T):
    person = {}
    N = int(input())
    idx = 0
    parent = [0] * 200000
    for i in range(200000):
        parent[i] = i

    number = [1] * 200000

    for _ in range(N):
        a,b = input().split()
        if a not in person.keys():
            person[a] = idx
            idx+=1
        if b not in person.keys():
            person[b] = idx
            idx+=1

        if find(person[a]) != find(person[b]):
            res = union(person[a],person[b])
        else :
            res = find(person[b])
        print(number[res])