# number = int(input())
# maxL = 0
# answer = []
# for i in range(1,number+1) : #i의 범위 지정 수정
#     res = [number] #첫번째 수를 포함한 배열을 만들고
#     res.append(i) #두번째 수를 넣어준다
#     j=1
#     while True :
#         tmp = res[j-1] - res[j]
#         if tmp < 0 : #뺄셈 결과가 음수이면 중지
#             if maxL < len(res) : #그때의 숫자 개수가 최대인 값을 찾는다
#                 maxL = len(res)
#                 answer = res[:]
#             break
#         res.append(tmp) #뺄셈이 0보다 크거나 같으면 그 결과를 배열에 넣어준다
#         j+=1 #인덱스에 1을 더해주고 반복 실행
#
# print(maxL)
# print(*answer)

number = int(input())

max_cnt = 0
res = []
for i in range(number+1) : # 두번째 숫자를 0부터 주어진 숫자까지 한번씩 다 넣어본다
    numbers = [number,i] # 첫번째 숫자와 두번째 숫자로 이루어진 배열
    new = numbers[0]-numbers[1] # 다음 숫자
    k=1 
    while new>=0 : # 만약 다음 숫자가 음수가 아니라면 
        numbers.append(new) # 배열에 넣어주고
        new = numbers[k]-numbers[k+1] # 새로운 다음 숫자를 구한다
        k+=1 
    if max_cnt<len(numbers) : # 모두 구한 다음에 만약 그 배열의 길이가 max값보다 길다면
        max_cnt = len(numbers) # 바꿔주고
        res = numbers # 그 때의 배열을 res에 넣어준다
print(max_cnt)
print(*res)
