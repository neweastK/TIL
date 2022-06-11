#3과 5로 이루어진 합이 N인 리스트 만들기
from itertools import combinations_with_replacement
N = int(input())
three = N//3 #봉지의 최대 갯수 (이 이상이면 못 만드는 것)
five = N//5 #봉지의 최소 갯수 (최소 이만큼의 봉지는 필요함)
arr = [3,5]
i = five
ans = 0
# ans가 변경되었다는 것은 최소 봉지 갯수를 찾았다는 것
while ans==0 :
    if i > three: #최대치를 넘어가면 못 만드는 것이므로 정답은 -1
        ans = -1
        break
    # 최소 봉지 갯수를 찾아야하므로, 총 봉지 개수를 최소부터 1씩 증가시키며 찾음
    subs=list(combinations_with_replacement(arr,i))
    for sub in subs :
        # 만약 무게 N을 만들어냈다면
        if sum(sub) == N :
            # 정답에 해당 봉지 개수를 배정
            ans = len(sub)
            break
    else :
        i+=1

print(ans)