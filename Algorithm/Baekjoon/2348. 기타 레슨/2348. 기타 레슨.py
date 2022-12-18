def check(size):
    cnt=0
    tmp = 0
    for num in nums:
        if tmp+num>size:
            tmp=num
            cnt+=1
        else:
            tmp+=num
    # print(size,cnt+1)
    return cnt+1

N,M = map(int,input().split())
nums = list(map(int,input().split()))

maximum = max(nums)
start = maximum
end = 10000*N
answer = 10**9
while start<=end:
    mid = (start+end)//2
    res = check(mid)
    if res>M:
        start=mid+1
    else:
        end=mid-1
        if answer>mid:
            answer = mid
print(answer)