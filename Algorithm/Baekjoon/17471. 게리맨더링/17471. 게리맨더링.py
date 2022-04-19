# 고립되지 않았는지 확인 (필요 없더라)
def near_district(A_list,B_list):
    if len(A_list) == len(B_list) == 1 :
        return True
    district = [0]*(N+1)
    for a in A_list :
        district[a] = 'A'
    for b in B_list :
        district[b] = 'B'

    for j in range(1,N+1):
        base = district[j] #체크할 구역의 선거구 (A or B)
        for c in connection[j] :
            if base == district[c] : #만약 기준 구역의 선거구와 연결 구역의 선거구가 같으면 ok니까 통과
                break
        else : #
            return False
    else :
        return True

# 선거구끼리 전체 구역이 연결되어있는지 확인
def check_connection(d_list):
    stack = [d_list[0]]
    visited = []
    while stack :
        now = stack.pop()
        if now not in visited and now in d_list:
            visited.append(now)
            stack.extend(connection[now])

    if len(set(visited)) == len(d_list):
        return True
    else :
        return False


def DFS(k,A_pop,B_pop, A_list,B_list): #구역번호, A선거구 인구합, B선거구 합
    global res
    if k==N+1:
        if A_list and B_list :

            if check_connection(A_list) and check_connection(B_list):
                if res > A_pop - B_pop >= 0 :
                    res = A_pop-B_pop
                    imsi = A_list
                    imsi2 = B_list
                return
            else :
                return

    else :
        DFS(k+1,A_pop,B_pop+population[k],A_list,B_list+[k])
        DFS(k+1,A_pop+population[k],B_pop,A_list+[k],B_list)

N = int(input())
population = [0]+list(map(int,input().split()))

# 구역간의 연결 관계를 나타내는 딕셔너리
connection = {}

for n in range(1,N+1):
    temp = list(map(int,input().split()))
    connection[n] = temp[1:]

res=9999
DFS(1,0,0,[],[])
if res == 9999 :
    res = -1
print(res)


