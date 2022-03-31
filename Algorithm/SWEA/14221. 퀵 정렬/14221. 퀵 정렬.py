# def quick_sort(lst, l, r):
#     if l < r:
#         pivot = partition(lst, l, r)
#         quick_sort(lst, l, pivot-1)
#         quick_sort(lst, pivot+1, r)
#
#
# def partition(lst,l,r):
#     pivot = (l+r)//2
#     i = l
#     j = r
#     while i<j :
#         while i<j and lst[i]<lst[pivot]:
#             i += 1
#         while i<j and lst[j]>=lst[pivot]:
#             j -= 1
#
#         if i < j :
#             if i == pivot :
#                 pivot = j
#             lst[i],lst[j] = lst[j],lst[i]
#         lst[pivot], lst[j] = lst[j], lst[pivot]
#     return j
def quick_sort(lst, l, r):

    if l < r:
        pivot = partition(lst, l, r)
        quick_sort(lst, l, pivot-1)
        quick_sort(lst, pivot+1, r)

def partition(lst,l,r):
    pivot = lst[r]
    i = l-1
    for j in range(l, r):
        if lst[j] <= pivot:
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[r], lst[i+1] = lst[i+1], lst[r]
    return i+1


T = int(input())
for tc in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    quick_sort(lst,0,len(lst)-1)
    print(f"#{tc+1} {lst[N//2]}")
