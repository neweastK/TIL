import sys
input = sys.stdin.readline

N = int(input())

max_arr = [0]*3
max_tmp = [0]*3

min_arr = [0]*3
min_tmp = [0]*3

for _ in range(N):
    a,b,c = map(int,input().split())

    max_tmp[0] = max(max_arr[0]+a,max_arr[1]+a)
    max_tmp[1] = max(max_arr[0]+b, max_arr[1]+b, max_arr[2]+b)
    max_tmp[2] = max(max_arr[1]+c, max_arr[2]+c)

    min_tmp[0] = min(min_arr[0]+a, min_arr[1]+a)
    min_tmp[1] = min(min_arr[0]+b, min_arr[1]+b, min_arr[2]+b)
    min_tmp[2] = min(min_arr[1]+c, min_arr[2]+c)


    for i in range(3):
        max_arr[i] = max_tmp[i]
        min_arr[i] = min_tmp[i]

ans = (max(max_arr), min(min_arr))
print(*ans)