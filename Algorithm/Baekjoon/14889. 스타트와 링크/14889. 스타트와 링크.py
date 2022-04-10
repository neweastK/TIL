from pprint import pprint
import time
def DFS(n,start,link):
    global ans
    if len(start) > N//2 or len(link) > N//2:
        return

    if n == N : # 모든 인원들의 능력치를 다 더했다면
        if len(start) == len(link): # 그리고 만약 두 팀에 인원이 균등하게 분배됐다면
            start_status = link_status = 0 # start팀 능력치와 link팀 능력치를 0으로 설정
            for i in range(N//2): # N명이면 각 팀 인원은 N//2일 것이므로 N//2에 range를 사용하여 그만큼 돌고
                for j in range(N//2) : # 이후 각각의 능력치를 더해준다
                    start_status+=arr[start[i]][start[j]]
                    link_status+=arr[link[i]][link[j]]

            res = abs(start_status-link_status)

            if res < ans : # 만약 결과값이 이전 결과값들보다 낮다면 바꿔준다.
                ans = res
        return

    else : # 아직 인원이 남았다면, start팀에 더해주는 경우와 link 팀에 더해주는 경우로 나눈다
        DFS(n+1,start+[n],link)
        DFS(n+1,start,link+[n])



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

ans= 999999
DFS(0,[],[])
print(ans)
