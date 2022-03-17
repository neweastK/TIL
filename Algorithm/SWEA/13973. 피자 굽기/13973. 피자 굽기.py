import sys
sys.stdin = open("input.txt")
from collections import deque

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    cheese = list(map(int,input().split())) #피자의 치즈양
    queue = deque() #화덕
    i=1 #피자 번호
    while len(queue) < N : #화덕의 크기만큼만 넣어준다
        queue.append([cheese.pop(0),i]) #피자의 치즈양과 피자 번호를 같이 넣어준다
        i+=1

    while len(queue) > 1 : #하나의 피자가 남을 때까지
        pizza = queue.popleft() #맨 앞 피자를 확인한다
        melt = pizza[0]//2 #한바퀴 도는 동안 녹고나서의 치즈양
        if melt : #아직 치즈가 남았다면
            queue.append([melt,pizza[1]]) #다시 넣어준다
        else : #치즈가 없다면
            if len(cheese) : #만약 아직 피자가 남았다면
                queue.append([cheese.pop(0),i]) #피자를 넣어준다
                i+=1

    print(f'#{tc+1} {queue[0][1]}')




    #


