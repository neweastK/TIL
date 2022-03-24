import sys
sys.stdin = open("input.txt")


def check_code(code):
    odd_num = even_num = 0
    for x in range(0,len(code),2) :
        odd_num += code[x] #홀수번째 값들의 합
        even_num += code[x+1] #짝수번째 값들의 합 (마지막 검증코드도 함께 계산)
    if (odd_num*3 + even_num) % 10 : #계산값이 10의 배수가 아니면 비정상적인 코드
        return 0
    else : #계산값이 10의 배수면 정상적인 코드
        return sum(code)


hex_rule = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

password = {
    "211": 0, "221": 1, "122": 2, "411": 3,
    "132": 4, "231": 5, "114": 6, "312": 7,
    "213": 8, "112": 9
}


T = int(input())

for tc in range(T) :
    N,E = map(int,input().split())
    arrs = [input().strip() for _ in range(N)]
    codes = []
    for arr in arrs :
        try :
            if sum(map(int,arr)) and arr not in codes:
                codes.append(arr)
        except ValueError :
            if arr not in codes :
                codes.append(arr)

    search_target = []
    for code in codes :
        res=[]
        nums = [int(c) if c not in hex_rule else hex_rule.get(c) for c in code]
        for j in range(len(nums)):
            bin_tmp = [0] * 4
            num = nums[j]
            k = 3
            while num > 0:
                bin_tmp[k] = num % 2
                num = num // 2
                k -= 1
            res += bin_tmp
        search_target.append("".join(map(str,res)).rstrip("0"))


    verify=[]
    answer = 0
    for target in search_target :
        result_code = []
        count_target = [0,0,0]
        for t in range(len(target)-1,-1,-1) :
            if target[t] == "1" and count_target[-2] == 0  :
                count_target[-1] += 1
            elif target[t] == "0" and count_target[-3] == 0 and count_target[-1]>0 :
                count_target[-2] += 1
            elif target[t] == "1" and count_target[-1] != 0 :
                count_target[-3] += 1
            elif target[t] == "0" and count_target[0] != 0 :
                if target[t-1] == "1" :
                    base = min(count_target)
                    new_count = "".join(map(str,[tar//base for tar in count_target]))
                    result_code.append(password.get(new_count))
                    count_target = [0, 0, 0]

            if len(result_code) == 8 :
                result_codes = result_code[::-1]
                if result_codes not in verify :
                    check_result = check_code(result_codes)
                    if check_result :
                        answer += check_result
                        verify.append(result_codes)
                result_code=[]

    print(f"#{tc+1} {answer}")