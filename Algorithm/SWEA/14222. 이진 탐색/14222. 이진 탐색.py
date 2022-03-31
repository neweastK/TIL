# 이진 탐색 함수 만들기
def binary_search(arr,l,r,target,direction):
    global cnt
    m = (l + r) // 2
    if len(direction)>1 and direction[-1] == direction[-2] : #만약 두번 연속 같은 방향으로 탐색했다면 탈락시킨다.
        return

    if arr[m]>target : # 왼쪽 탐색 (중간값>목표값)
        binary_search(arr,l,m-1,target,direction+["L"])
    elif arr[m]<target : # 오른쪽 탐색 (중간값<목표값)
        binary_search(arr,m+1,r,target,direction+["R"])
    else : #중간값=목표값 개수 추가
        cnt+=1


T = int(input())

for tc in range(T):
    N,M = map(int,input().split())

    N_list = sorted(list(map(int,input().split())))
    M_list = list(map(int,input().split()))

    #M의 원소들이 N에 있는가. 그리고 있다면 좌우로 탐색하거나 중앙에 있는가
    cnt = 0
    for num in M_list :
        binary_search(N_list,0,N-1,num,[])
    print(f'#{tc+1} {cnt}')