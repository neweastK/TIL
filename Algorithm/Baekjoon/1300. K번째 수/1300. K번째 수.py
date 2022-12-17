def check_k(target):
    # idx는 target보다 작은 숫자들의 개수
    idx = 0
    for i in range(1, N + 1):
        idx += min(target//i, N)
    return idx

N = int(input())
k = int(input())

start = 1
end = N**2
mid = (start+end)//2

while start<=end:
    mid = (start+end)//2
    target_range = check_k(mid)
    if target_range>=k:
        end = mid-1
        answer = mid
    else:
        start = mid+1
print(answer)
