# from collections import deque

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst)//2

    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    # return merge(deque(left), deque(right))
    return merge(left, right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt+=1

    result = []

    ### 인덱싱을 활용하는 경우
    i=j=0
    while i<len(left) or j<len(right) :
        if i<len(left) and j<len(right) :
            if left[i] < right[j] :
                result.append(left[i])
                i+=1
            else :
                result.append(right[j])
                j+=1
        elif i<len(left) :
            result.extend(left[i:])
            break
        elif j < len(right):
            result.extend(right[j:])
            break

    ### deque를 사용하는 경우
    # while left or right:
    #
    #     if left and right:
    #         if left[0] <= right[0]:
    #             result.append(left.popleft())
    #         else:
    #             result.append(right.popleft())
    #     elif left:
    #         result.extend(left)
    #         break
    #     elif right:
    #         result.extend(right)
    #         break

    return result

T = int(input())
for tc in range(T):
    cnt=0
    N=int(input())
    lst = list(map(int,input().split()))
    result = merge_sort(lst)
    print(f"#{tc+1} {result[N//2]} {cnt}")
