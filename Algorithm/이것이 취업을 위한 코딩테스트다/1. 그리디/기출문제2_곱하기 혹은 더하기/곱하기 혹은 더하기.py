nums = "01122"

"""
res=1
for num in nums :
    if int(num) <= 1 :
        res += int(num)
    else :
        res *= int(num)        
"""

res=int(nums[0])

for num in nums[1:]:
    sum_value = res+int(num) # 더해줬을 때
    times_value = res*int(num) # 곱해줬을 때
    res = sum_value if sum_value>times_value else times_value # 더 큰 값을 res로 넣고 다시 반복
print(res)