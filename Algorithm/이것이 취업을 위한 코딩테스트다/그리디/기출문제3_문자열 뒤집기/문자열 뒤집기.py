str_nums = ['0001100','11111','00000001','11001100110011000001','11101101']


for str_num in str_nums :
    temp_one = str_num.split('0') #1으로 이루어진 문자열이 나오고 나머지는 ''로 나옴
    count_one = (len(temp_one)-temp_one.count('')) # 1로 이루어진 집합의 개수

    temp_zero = str_num.split('1') #0으로 이루어진 문자열이 나오고 나머지는 ''로 나옴
    count_zero = (len(temp_zero)-temp_zero.count('')) # 0으로 이루어진 집합의 개수

    ans = count_zero if count_zero<count_one else count_one
    print(ans)

