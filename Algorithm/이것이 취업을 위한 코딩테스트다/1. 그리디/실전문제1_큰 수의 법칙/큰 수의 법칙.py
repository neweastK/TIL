N, M, K = 5, 8, 3

nums = [2,4,5,4,6]

#가장 큰 수 두개를 구한다.
first = max(nums)
nums.remove(first)
second = max(nums)

# res=0
# cnt=0
# for _ in range(M):
#     if cnt==K :
#         res+=second
#         cnt=0
#     else :
#         res+=first
#         cnt+=1
# print(res)

res=0
set_times = M//(K+1)
others = M&(K+1)
res += (K*first+second)*set_times
res += others*first

print(res)
