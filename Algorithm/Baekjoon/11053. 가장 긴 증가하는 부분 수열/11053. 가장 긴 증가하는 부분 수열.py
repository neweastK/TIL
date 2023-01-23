# 원본 배열 값을 탐색하기 위한 이분탐색 함수
def bin_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if res[mid] > target:
            end = mid - 1
        elif res[mid] == target:
            return mid
        else:
            start = mid + 1
    return start


N = int(input())
arr = list(map(int, input().split()))
# LIS의 길이를 구할 배열
res = [arr[0]]

# 원본 배열 값의 적정 위치 찾아주기
for a in arr:
    # 만약 원본 배열 값이 res에 있는 모든 값보다 크다면
    if a > res[-1]:
        # append
        res.append(a)
    # 아니라면 해당 값의 위치를 찾아줌
    else:
        tmp = bin_search(0, len(res), a)
        # 해당 값을 원본 배열 값으로 바꿔준다
        res[tmp] = a

print(len(res))
