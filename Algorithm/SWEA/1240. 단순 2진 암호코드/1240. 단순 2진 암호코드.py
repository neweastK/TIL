# 암호비트패턴
password = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9
}

# 마지막에 정상적인 암호코드인지 확인하기 위한 함수
def check_code(code):
    odd_num = even_num = 0
    for x in range(0,len(code),2) :
        odd_num += code[x] #홀수번째 값들의 합
        even_num += code[x+1] #짝수번째 값들의 합 (마지막 검증코드도 함께 계산)
    if (odd_num*3 + even_num) % 10 : #계산값이 10의 배수가 아니면 비정상적인 코드
        return 0
    else : #계산값이 10의 배수면 정상적인 코드
        return sum(code)

T=int(input())

for tc in range(T):

    N,M=map(int,input().split())

    codes = [input() for _ in range(N)] #주어진 배열

    password_code = ""
    for code in codes :
        if "1" in code : #배열 중 한줄에 1이 있는 배열이 있다면
            password_code+=code #password_code에 넣어주고
            break #중단 (어차피 다 똑같기 때문에)

    loc_end = 0
    for i in range(M-1,-1,-1) : #1이 어디있는지 찾을 때 뒤에서부터 찾는다(모든 암호패턴이 1로 끝나기 때문에)
        if password_code[i] == "1":
            loc_end = i #처음으로 1을 찾는 부분이 맨끝
            loc_start = i-55 #총 길이는 56이므로 시작점도 알 수 있음
            break #맨 뒤 1 하나만 찾으면 되므로 break
    real_code = password_code[loc_start:loc_end+1] #지정해준 범위로 새로운 변수에 할당

    result = []
    j=0
    while j <= len(real_code)-7 : #7개씩 끊어서
        if real_code[j:j+7] in password : #암호패턴에 맞는 숫자 찾기
            result.append(password.get(real_code[j:j+7])) #맞는 숫자를 result에 넣어준다
            j+=7
        else :
            j+=1

    print(f'#{tc+1} {check_code(result)}') #함수를 통해 결과값 반환
