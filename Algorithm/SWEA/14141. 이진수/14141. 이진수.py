import sys

sys.stdin = open("input.txt")

# 16진수 규칙(알파벳일 때)
hex_rule = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

T = int(input())

for tc in range(T):
    N, hex_nums = input().split()
    res = []
    # 16진수 각각의 문자를 10진수로 바꿔서 리스트에 넣어준다
    nums = [int(hex_num) if hex_num not in hex_rule else hex_rule.get(hex_num) for hex_num in hex_nums]
    # 10진수로 바뀐 수를 다시 2진수로 바꿔준다.
    for i in range(int(N)):
        tmp = [0] * 4  # 16진수 한개의 글자를 4개의 이진수 글자로 바꿔야하므로 4개짜리 0으로 찬 리스트를 만들어준다.
        num = nums[i]
        j = 3
        while num > 0:
            tmp[j] = num % 2
            num = num // 2
            j -= 1
        res += tmp

    print(f'#{tc + 1}', end=" ")
    for k in res:
        print(k, end="")
    print()
