import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T) :
    N = int(input())

    arr = [None]+[0]*N
    values = list(map(int,input().split()))

    i=1
    for value in values :
        arr[i] = value
        k=i
        while k>1 :
            if arr[k//2] > arr[k] :
                arr[k//2],arr[k] = arr[k],arr[k//2]
                k=k//2

            else:
                break
        i+=1

    res = 0
    d = len(arr)-1
    while d//2:
        res+=arr[d//2]
        d = d//2
    print(f'#{tc+1} {res}')