N = int(input())
cranes = list(map(int,input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    cnt = 0

    while boxes:
        for i in cranes:
            for j in boxes:
                if i<j:
                    continue
                else:
                    boxes.remove(j)
                    break

        cnt += 1
    print(cnt)