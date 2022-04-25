nums = input()
part1 = nums[:len(nums)//2]
part2 = nums[len(nums)//2:]

sum1 = sum(map(int, part1))
sum2 = sum(map(int, part2))

if sum1 == sum2 :
    print("LUCKY")
else :
    print("READY")
