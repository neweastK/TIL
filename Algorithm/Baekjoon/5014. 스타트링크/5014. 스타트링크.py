from collections import deque
import sys
input = sys.stdin.readline


def bfs(queue) :

    global visited

    while queue :
        cf = queue.popleft()
        if cf == G :
            return

        for i in (U,-D) :
            nf = cf+i
            if 0<nf<=F and visited[nf] == 0 :
                visited[nf] = 1
                counted[nf] = counted[cf]+1
                queue.append(nf)

F,S,G,U,D = map(int,input().split())

visited = [0] * (F+1)
counted = [-1] * (F+1)
start = deque([S])
visited[S] = 1
counted[S] = 0
bfs(start)
if counted[G] == -1 :
    print('use the stairs')
else :
    print(counted[G])