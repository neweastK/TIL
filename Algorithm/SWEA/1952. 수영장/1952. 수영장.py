import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T) :
    prices = list(map(int,input().split()))
    plans = list(map(int,input().split())) + [0]*3
    total = [0] * 15

    total[0] = min(prices[0] * plans[0], prices[1])
    for i in range(1, len(plans)):
        total[i] = total[i-1] + min(prices[0] * plans[i],prices[1])

        if i >= 2:
            total[i] = min(total[i], total[i-3] + prices[2])

    if total[-1] < prices[-1] :
        print(f"#{tc+1} {total[-1]}")
    else :
        print(f"#{tc+1} {prices[-1]}")



