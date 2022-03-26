import time
import sys
sys.stdin = open("input.txt")
# 재귀로 했더니 시간 초과...

# def DFS(N,total) :
#     global cnt
#     if N<total :
#         return
#     elif N == total:
#         cnt+=1
#         return
#     else:
#         DFS(N,total+10)
#         DFS(N,total+20)
#         DFS(N,total+20)
#
# T = int(input())
#
# for tc in range(T):
#     cnt=0
#     N = int(input())
#     DFS(N,0)
#     print(f'#{tc+1} {cnt}')



# # DP를 할 때는 점화식을 찾자
# def DP(N):
#     if N==10 :
#         return 1
#     elif N==20 :
#         return 3
#     else :
#         return 2*DP(N-20) + DP(N-10)
#
#
# T = int(input())
# for tc in range(T):
#     result =DP(int(input()))
#     print(f"#{tc+1} {result}")


# 메모이제이션 활용

# def DP(N):
#     global memo
#     if N == 10 or N==20:
#         return memo[N]
#     else :
#         return 2*DP(N-20) + DP(N-10)
#
# start = time.time()
# T = int(input())
# for tc in range(T):
#     N=int(input())
#     memo = [0]*N
#     memo[10] = 1
#     memo[20] = 3
#     result =DP(N)
#     print(f"#{tc+1} {result}")


