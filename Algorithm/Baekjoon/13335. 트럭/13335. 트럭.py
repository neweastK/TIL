from collections import deque
import sys
input = sys.stdin.readline

N,W,L = map(int,input().split())
trucks = deque(list(map(int,input().split())))
bridge = deque([])
time = 0

while True:
    if len(trucks) == 0 and sum(bridge) == 0 :
        break
    time+=1
    # 다리가 꽉 찼다면 도착지 앞의 트럭 빼주기
    if len(bridge) == W :
        bridge.popleft()
    # 새로 출발할 트럭이 없다면?
    if len(trucks) == 0 :
        bridge.append(0)

    # 아직 트럭이 있고 무게 제한에 안걸린다면?
    elif sum(bridge)+trucks[0] <= L :
        truck = trucks.popleft()
        bridge.append(truck)

    # 아직 트럭은 있는데 무게 제한에 걸린다면?
    else :
        bridge.append(0)

print(time)
