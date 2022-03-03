number = int(input())
maxL = 0
answer = []
for i in range(1,number+1) : #i의 범위 지정 수정
    res = [number] #첫번째 수를 포함한 배열을 만들고
    res.append(i) #두번째 수를 넣어준다
    j=1
    while True :
        tmp = res[j-1] - res[j]
        if tmp < 0 : #뺄셈 결과가 음수이면 중지
            if maxL < len(res) : #그때의 숫자 개수가 최대인 값을 찾는다
                maxL = len(res)
                answer = res[:]
            break
        res.append(tmp) #뺄셈이 0보다 크거나 같으면 그 결과를 배열에 넣어준다
        j+=1 #인덱스에 1을 더해주고 반복 실행

print(maxL)
print(*answer)