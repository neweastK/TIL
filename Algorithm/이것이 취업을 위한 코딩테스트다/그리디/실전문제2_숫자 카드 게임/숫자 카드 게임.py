N, M = 3, 3
# N, M = 2,4
arr1 = [[3,1,2],[4,1,4],[2,2,2]]
arr2 = [[7,3,1,8],[3,3,3,4]]
candidate=[]
for arr in arr2 :
    candidate.append(min(arr))

print(max(candidate))
