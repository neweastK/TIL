# 열 위치를 숫자로 표현하기 위한 딕셔너리
column_chg = {
    'a':1,'b':2,'c':3,'d':4,
    'e':5,'f':6,'g':7,'h':8,
}
# 우,좌,하,상
dx = [0,0,1,-1]
dy = [1,-1,0,0]

loc = input()
x,y = int(loc[1]), column_chg[loc[0]]
cnt=0

for d1 in range(4):
    nx = x+(dx[d1]*2)
    ny = y+(dy[d1]*2)
    # 현재 이동한 방향이 수직이면 다음 이동은 수평으로
    # 현재 이동한 방향이 수평이면 다음 이동은 수직으로 할 수 있도록 한다
    next = [2,3] if d1<=1 else [0,1]
    for d2 in next:
        final_x = nx+dx[d2]
        final_y = ny+dy[d2]
        if 1<=final_x<9 and 1<=final_y<9 :
            cnt+=1

print(cnt)

# 추가 테스트 케이스
# a7 = 3 , g1=3