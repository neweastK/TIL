import sys
sys.stdin = open("input.txt")



def merge_sort(lst):
    if len(lst) == 1:
        return lst

    # 문제에서 제시해준 그룹을 나누는 방법
    middle = (len(lst)+1)//2
    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    winner = []
    # 무승부일 때는 번호가 더 작은 쪽이 승자가 된다
    if left[0][1] == right[0][1] :
        winner = left if left[0][0]<right[0][0] else right

    # 왼쪽이 가위일 때
    elif left[0][1] == 1 and right[0][1] == 2 :
        winner = right
    elif left[0][1] == 1 and right[0][1] == 3:
        winner = left
    # 왼쪽이 바위일 때
    elif left[0][1] == 2 and right[0][1] == 3:
        winner = right
    elif left[0][1] == 2 and right[0][1] == 1:
        winner = left
    # 왼쪽이 보일 때
    elif left[0][1] == 3 and right[0][1] == 1:
        winner = right
    elif left[0][1] == 3 and right[0][1] == 2:
        winner = left

    return winner

T = int(input())

for tc in range(T):
    N = int(input())
    lst_input = list(map(int,input().split()))
    lst = list(enumerate(lst_input)) # 카드 목록을 카드 번호와 함께 나타내도록 한다.
    ans = merge_sort(lst)
    print(f"#{tc+1} {ans[0][0]+1}")