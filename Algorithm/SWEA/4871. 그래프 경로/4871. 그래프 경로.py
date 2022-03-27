from pprint import pprint
T = int(input())

for tc in range(T) :
    V,E = map(int,input().split())
    nodes = [ [][:] for _ in range(V+1)]
    for _ in range(E) :
        x,y = map(int,input().split())
        nodes[x].append(y)

    S,G = map(int,input().split())

    stack = [S]
    visited = [S]

    while stack:  # stack에 무언가가 있다면 반복

        tmp = stack[-1]  # 스택의 가장 위에 위치한 아이
        for value in nodes[tmp]:  # 그 노드가 갖고 있는 자식 노드들 중
            if value not in visited:  # 아직 방문하지 않았다면
                stack.append(value)  # 스택에 추가해주고
                visited.append(value)  # 방문했다고 표시해준다
                break  # DFS이므로 break!! 더 깊이 가야되니까!
        else:  # 반복문을 무사히 다 돌았다는 것 = 방문하지 않은 자식노드가 없다!
            stack.pop()  # pop을 통해 다른 노드로 이동

    if G in visited:
        print(f'#{tc + 1} {1}')
    else:
        print(f'#{tc + 1} {0}')