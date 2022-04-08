import sys
sys.stdin = open("input.txt")
from itertools import permutations

T = int(input())

for tc in range(T) :
    N = int(input())
    operators = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    oper_lst = ["+"]*operators[0] + ["-"]*operators[1] + ["*"]*operators[2] + ["/"]*operators[3]

    opers = set(permutations(oper_lst))
    res = []


    for oper in opers :
        tmp = nums[0]
        for i in range(1,len(nums)) :
            if oper[i-1] == "+":
                tmp += nums[i]
            elif oper[i-1] == "-":
                tmp -= nums[i]
            elif oper[i-1] == "*":
                tmp *= nums[i]
            else:
                tmp = int(tmp / nums[i])
        res.append(tmp)

    result = max(res) - min(res)
    print(f"#{tc+1} {result}")
