def check_key(N,M,arr,key, hole):
    for i in range(N+(2*(M-1))-(M-1)):
        for j in range(N+(2*(M-1))-(M-1)):
            lock_hole = hole
            for k in range(M):
                for l in range(M):
                    if arr[i+k][j+l] == 9 :
                        continue
                    elif arr[i+k][j+l] == 0 and key[k][l] == 1:
                        lock_hole -= 1
                    elif arr[i+k][j+l] == 1 and key[k][l] == 0:
                        continue
                    elif (arr[i+k][j+l] == 1 and key[k][l] == 1) or (arr[i+k][j+l] == 0 and key[k][l] == 0):
                        res = 'false'
                        break

                if (arr[i+k][j+l] == 1 and key[k][l] == 1) or (arr[i+k][j+l] == 0 and key[k][l] == 0):
                    res = 'false'
                    break
            else :
                if lock_hole == 0 :
                    res='true'
                    return res
    return res


def solution(key, lock):
    M = len(key)
    N = len(lock)
    lock_hole = 0
    for li in range(N):
        for lj in range(N):
            if lock[li][lj] == 0:
                lock_hole +=1
    else :
        if lock_hole == 0 :
            return True

    #새로운 배열
    new_arr = [[9]*(N+(2*(M-1))) for _ in range(N+(2*(M-1)))]

    #lock 배열을 새로운 배열에 넣기
    for ci in range(M-1,M-1+N):
        for cj in range(M-1,M-1+N):
            new_arr[ci][cj] = lock[ci-(M-1)][cj-(M-1)]


    for r in range(3):
        res = check_key(N, M, new_arr, key, lock_hole)
        if res == 'true':
            return True
        else :
            key = [t[::-1] for t in list(map(list,zip(*key)))]
    else :
        return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))

# test = [[1,1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# test1 = [t[::-1] for t in list(map(list,zip(*test)))]
# test2 = [t[::-1] for t in list(map(list,zip(*test1)))]
# test3 = [t[::-1] for t in list(map(list,zip(*test2)))]
# test4 = [t[::-1] for t in list(map(list,zip(*test3)))]
# print(test1)
# print(test2)
# print(test3)
# print(test4)
