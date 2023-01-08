import sys
sys.setrecursionlimit(10**9)

S = input()
T = input()
length = len(S)
ans = 0
def add_A(target):
    return target[:-1]

def add_B(target):
    target = target[:-1]
    return target[::-1]

def check(start):
    global ans
    if len(start)<=length:
        if start == S:
            ans = 1
            return
    else:
        if start[-1] == "A":
            res = add_A(start)
        else:
            res = add_B(start)

        check(res)

check(T)
print(ans)
