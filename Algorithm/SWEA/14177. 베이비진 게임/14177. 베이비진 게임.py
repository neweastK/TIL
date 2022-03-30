import sys
sys.stdin = open("input.txt")

# run, triplet이 있는지 확인하기
def check_run(card,combi,idx):
    # run이나 triplet을 담을 빈 리스트
    if len(combi) == 3 : # 갖고 있는 카드 중 세장을 뽑아서
        if len(set(combi)) == 1 : # 만약 세장의 카드가 모두 같은 값이면
            res.append(1) #triplet을 넣어주려 했는데 오류가 난다. 1을 넣어주자
        else : # 세장의 카드가 모두 같은 값이 아닐 때
            new_combi = sorted(combi) #오름차순으로 정렬을 해주고
            for i in range(1,3) : # 3장의 카드가 연속인지 확인한다
                if new_combi[i-1]+1 != new_combi[i] : #연속이 아니면
                    break #중단
            else : #무사히 모두 돌면 즉, 연속이면
                res.append(2) #run을 넣어주려 했는데 오류가 나서 2를 넣어줬다

    else : # 조합을 구한다.
        for j in range(idx,len(card)):
            combi.append(card[j])
            check_run(card,combi,j+1)
            combi.pop()



T = int(input())

for tc in range(T):
    cards = list(map(int,input().split()))
    card_a = [] #a의 카드
    card_b = [] #b의 카드
    ans = 0
    for x in range(0,len(cards),2):
        res = [] # 함수에서 결과값을 넣을 빈 리스트

        card_a.append(cards[x])
        if len(card_a) >= 3 : # a의 카드가 3장 이상이면
            check_run(card_a,[],0) #run,triplet을 확인한다
            if res : # res에 어떠한 값이 있다면
                ans = 1 # a가 이긴 것(b보다 먼저 나왔으므로)
                break

        # 위 과정과 똑같음
        res = []
        card_b.append(cards[x+1])
        if len(card_b) >= 3 :
            check_run(card_b,[],0)
            if res :
                ans = 2
                break

    print(f'#{tc+1} {ans}')

