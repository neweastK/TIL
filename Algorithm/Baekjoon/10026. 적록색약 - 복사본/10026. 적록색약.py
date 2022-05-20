N = int(input())
time_table = [list(map(int,input().split())) for _ in range(N)]

time_table.sort(key=lambda x:x[0])

classroom = [time_table[0][1]]
for time in time_table[1:] :
    i = 0
    while True:
        if i >= len(classroom) :
            classroom.append(time[1])
            break
        elif time[0] >= classroom[i] :
            classroom[i] = time[1]
            break
        else :
            i+=1

print(classroom)
print(len(classroom))


