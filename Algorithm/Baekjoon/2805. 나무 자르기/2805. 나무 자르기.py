import sys
input = sys.stdin.readline

def cut_tree(height):
    total = sum(map(lambda x:x-height if x>height else 0,trees))
    return total

N,M = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()

start = 0
end = trees[-1]
answer = 0

while start<=end:
    mid = (start+end)//2
    total = cut_tree(mid)
    if total>=M:
        start = mid+1
        answer = mid
    else:
        end = mid-1
print(answer)

