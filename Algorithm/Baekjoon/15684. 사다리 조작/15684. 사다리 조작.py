from itertools import combinations
import sys
input = sys.stdin.readline

# 사다리 타고 이동해보기
def check_answer(maps,start_n):
    x,y = start_n,1
    # 가로선 끝까지 갈 때까지
    while y<=H:
        if maps[x][y] == 1:
            x+=1
            y+=1
        elif maps[x][y] == 2:
            x-=1
            y+=1
        else:
            y+=1
    # 출발지와 도착지가 같은 경우 true 반환
    if start_n==x:
        return True
    else:
        return False

# 사다리를 추가하고 추가했을 때, 정답이 될 수 있는지 확인
def add_ladder(maps, ladders):
    for ladder in ladders:
        aa, bb = ladder
        maps[aa][bb] = 1
        maps[aa + 1][bb] = 2
    for i in range(1, N + 1):
        if not check_answer(maps,i):
            return False
    return True

N,M,H = map(int,input().split())
maps = [[0]*(H+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    # 나중에 조작할 사다리 위치를 줄이기 위한 사전작업
    if maps[b-1][a] == 0:
        maps[b-1][a] = -1
    # 사다리 연결
    # 왼쪽에서 오른쪽으로 이동
    maps[b][a] = 1
    # 오른쪽에서 왼쪽으로 이동
    maps[b+1][a] = 2

# 초반 검색
first_check = True
for i in range(1,N+1):
    if not check_answer(maps,i):
        first_check = False

if first_check:
    print(0)
else:
    # 조작 가능한 곳 찾기
    replace_area = []
    # 마지막 줄에는 사다리를 어차피 추가할 수 없음(i번째 사다리면 i+1번째 사다리도 필요하기 때문)
    for n in range(1,N):
        for m in range(1,H+1):
            if maps[n][m] == 0:
                replace_area.append([n,m])
    # 조작
    # 3번까지만 수정해보면 되므로 나머지는 모두 예외처리
    for k in range(1,4):
        # combinations 으로 바꿀 수 있는 위치 경우의 수를 모두 저장
        replace_list = list(combinations(replace_area,k))
        # 반복하면서 사다리를 수정해보고 조건에 맞는지 확인
        for replace_idx in replace_list:
            tmp_maps = [map[:] for map in maps]
            res = add_ladder(tmp_maps,replace_idx)
            if res:
                print(k)
                quit()
    else:
        print(-1)