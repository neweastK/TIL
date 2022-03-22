
def in_order(v): # 노드 번호를 이진탐색트리 탐색 순서로 정렬시키는 함수
    global order # 노드의 번호를 값을 기준으로 오름차순 정렬(맨 왼쪽 노드가 제일 작다!)
    if tree[v] : # v는 부모 노드 번호 즉, 부모 노드가 자식 노드를 갖고 있다면
        in_order(tree[v][0]) #왼쪽 자식 노드 함수 실행
        order.append(v) #그 다음 본인을 order에 append
        if tree[v][1] : #오른쪽 자식 노드가 있는 경우에만 실행
            in_order(tree[v][1])
    else :
        order.append(v) #자식 노드가 없는 경우


def make_tree(N):
    tree = [0]*(N+1) #맨 앞 0을 제외한 N개의 리스트
    i=1
    while i <= N//2 :
        if 2*i+1>N: # 자식 노드가 한개인 경우 / 즉, 오른쪽 노드의 번호가 N보다 클 경우
            tree[i] = (2*i,0) # 왼쪽 노드만 넣어준다
            break
        else :
            tree[i] = (2 * i, 2*i+1) #i번 부모 노드의 자식노드들의 위치 삽입
        i+=1 # 다음 부모 노드 찾기

    return tree



N = int(input())
order = [0] # 순서를 담을 리스트
tree = make_tree(N) #부모 노드의 자식노드 현황 생성
in_order(1)
res_tree = [0]*(N+1) # 최종 결과를 담을 트리
for i in range(1,N+1) :
    res_tree[order[i]] = i
    #order의 1번 값이 4라면 1의 위치는 4번째 이므로 res_tree의 4번째에 1을 넣어준다.

print(f'연결된 자식 노드:{tree}')
print(f'값이 작은 노드 : {order}')
print(f'#{res_tree} {res_tree[1]} {res_tree[N//2]}')