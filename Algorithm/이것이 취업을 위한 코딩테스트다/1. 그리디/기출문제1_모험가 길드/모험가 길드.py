N = 6
#낮은 숫자부터 grouping해야 그룹을 가장 많이 만들 수 있을 듯
people = [2,4,3,2,2,1]

#그 숫자만큼 슬라이싱. 그 안에 그 슬라이싱한 길이보다 큰 수가 있으면 fail
#일단 1은 무조건 하나이니 1은 제외

people.sort()
cnt=0
i=0
k = people[i]
while i+k<=N :
    group = people[i:i+k]
    if group[-1] > len(group) :
        k = group[-1]
    else :
        cnt+=1
        i = i+k
        if i >= N :
            break
        k = people[i]

print(cnt)