'''
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
'''
def binary_search(arr,start,end,target) :
    if start > end :
        return -1
    mid = (start+end)//2
    if arr[mid] == target :
        return mid
    elif arr[mid] > target :
        return binary_search(arr,start,mid-1,target)
    elif arr[mid] < target :
        return binary_search(arr,mid+1, end, target)


def left_count(arr,base,target) :
    global cnt
    left = base-1
    while left >= 0 and arr[left] == target :
        cnt += 1
        left -=1

def right_count(arr,base,target) :
    global cnt
    right = base+1
    while right < N and arr[right] == target :
        cnt += 1
        right +=1



N, x = map(int, input().split())
numbers = list(map(int,input().split()))
res = binary_search(numbers,0,N-1,x)

if res>=0 :
    cnt = 1
    left_count(numbers,res,x)
    right_count(numbers,res,x)
    answer = cnt
else :
    answer = -1

print(answer)

