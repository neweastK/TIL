len_x, len_y = map(int,input().split())
C = int(input())
cut_x = [0]
cut_y = [0]
for _ in range(C) : # 자르는 모든 경우를 모은다
    d,loc = map(int,input().split())
    if d : # 세로로 자르면
        cut_y.append(loc)
    else : # 가로로 자르면
        cut_x.append(loc)

cut_x.sort()
cut_y.sort()

# 가로로 자르는 것은 세로와 관련이 있고, 세로로 자르는 것은 가로와 연관이 있음
cut_x.append(len_y)
cut_y.append(len_x)

# 다 자르고 나서의 최댓값들 구하기
max_y = 0
max_x = 0
# 자를 위치들을 모은 후 가장 앞의 위치부터 잘랐을 때의 길이를 각각 구한다.
for i in range(len(cut_x)-1) :
    tmp_y = cut_x[i+1]-cut_x[i]
    if tmp_y>max_y :
        max_y = tmp_y

for j in range(len(cut_y)-1) :
    tmp_x = cut_y[j+1]-cut_y[j]
    if tmp_x>max_x :
        max_x = tmp_x

print(max_x*max_y)

