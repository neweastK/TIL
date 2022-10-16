import sys
input = sys.stdin.readline

N = input().rstrip()

dp = [0]*5001
dp[0] = 1
dp[1] = 1

# 0이 맨 앞이면 무조건 오류
if N[0] == "0" :
    dp[len(N)] = 0
else :
    for i in range(1,len(N)):
        if N[i] == "0" :
            if N[i-1] == "0":
                dp[len(N)] = 0
                break
            else :
                # 앞 숫자와 묶은게 30이상일 경우
                if int(N[i-1]) > 2:
                    dp[len(N)] = 0
                    break
                else :
                    dp[i+1] = dp[i-1]
        else :
            if N[i-1] == "0":
                dp[i+1] = dp[i]
            else:
                if int(N[i-1:i+1]) <= 26:
                    dp[i+1] = dp[i-1]+dp[i]
                else :
                    dp[i+1] = dp[i]
print(dp[len(N)]%1000000)
