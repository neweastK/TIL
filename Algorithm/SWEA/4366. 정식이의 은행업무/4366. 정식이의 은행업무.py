# 2진수 값과 3진수 값이 일치했을 때의 값 찾기
def money(bin_num, third_num) :
    for i in range(len(bin_num)) : # 2진수 값부터 한 자리씩 수정
        tmp_bin = bin_num[:] # 다음 자리를 바꿀 때 원래 리스트로 돌아와야하기 때문에 따로 저장
        tmp_bin[i] = abs(tmp_bin[i] - 1) # 1은 0으로 0은 1로 바꿔준다
        bin_test = 0 # 2진수를 10진수로 바꿔줄 변수
        for x in range(len(tmp_bin)): # 2진수 값을 10진수로 바꾸기
            bin_test += tmp_bin[x] * (2 ** (len(tmp_bin)-1-x))

        #위에서 나온 값과 3진수 내에서 하나씩 바꾼 값을 비교한다
        for j in range(len(third_num)) :
            tmp_third = third_num[:] # 다음 자리를 바꿀 때 원래 리스트로 돌아오기
            for k in range(3) : # 3진수는 한자리를 0,1,2 로 바꿀 수 있으므로 3번 변경 필요
                tmp_third[j] = k # 바꿔주고
                third_test = 0
                for y in range(len(tmp_third)) : # 3진수 값을 10진수로 바꿔준다
                    third_test += tmp_third[y] * 3**(len(tmp_third)-1-y)

                # 만약 2진수에서 나온 값과 3진수에서 나온 값이 같다면 해당 값을 return
                if bin_test == third_test :
                    return bin_test


T = int(input())

for tc in range(T) :

    # 값을 바꿔줄 수 있도록 list로 받는다
    bin_num = list(map(int,input()))
    third_num = list(map(int,input()))

    result = money(bin_num, third_num)
    print(f'#{tc+1} {result}')



