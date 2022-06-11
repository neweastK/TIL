X = int(input())

arr = [1]
d = 1
while arr[-1]<10000000 :
    arr.append(arr[-1]+d)
    d += 1

tmp = 0
for i in range(len(arr)):
    if X<arr[i]:
        tmp = i-1
        break

# 첫 시작하는 값과의 차이
gap = X-arr[tmp]
# i가 짝수이면 분자는 i+1부터 그리고 분모는 1부터
if tmp % 2 == 0 :
    # 분모는 1+차이
    parent = 1+gap
    child = tmp+1-gap
else :
    parent = tmp+1-gap
    child = 1+gap
print(f'{child}/{parent} ')