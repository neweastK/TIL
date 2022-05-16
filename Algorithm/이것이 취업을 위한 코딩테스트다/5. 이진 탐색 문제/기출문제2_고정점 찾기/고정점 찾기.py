'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''

def binary_search(arr,start,end) :
    if start > end :
        return -1
    mid = (start+end) // 2
    if arr[mid] == mid :
        return mid
    elif arr[mid] > mid :
        return binary_search(arr,start,mid-1)
    else :
        return binary_search(arr,mid+1,end)

N = int(input())
numbers = list(map(int,input().split()))
res = binary_search(numbers, 0, N-1)
print(res)
