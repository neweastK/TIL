import sys
from itertools import product
input = sys.stdin.readline

numbers = ['0','1','2','3','4','5','6','7','8','9']

now = 100
N = int(input())
c = int(input())
plus_minus = abs(now-N)

if c == 0 :
    ans = plus_minus if plus_minus < len(str(N)) else len(str(N))
    print(ans)

else :

    broken = list(input().split())

    usable = list(set(numbers)-set(broken))
    print(usable)
    # 모든 버튼이 고장난 경우
    if len(usable) == 0 :
        print(plus_minus)
    else :
        num_list = list(product(usable, repeat=len(str(N))))+list(product(usable, repeat=len(str(N))+1))+list(product(usable, repeat=len(str(N))-1))
        print(num_list)
        min_gap = int(1e9)
        closet_num = N
        for num in num_list :
            if len(num) == 0 :
                continue
            tmp = int(''.join(num))
            gap = abs(tmp-N)
            if min_gap > gap :
                min_gap = gap
                closet_num = tmp
            elif min_gap == gap :
                closet_num = tmp if len(str(tmp)) < len(str(closet_num)) else closet_num
        button_gap = abs(closet_num-N)
        final = len(str(closet_num)) + button_gap
        if final < plus_minus :
            res = final
        else :
            res = plus_minus
        print(res)