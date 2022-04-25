sentence = input()

#입력값에서 숫자와 문자열의 분리를 위한 리스트 생성
num = []
string = []

#입력값을 순회하면서 문자열인지 숫자인지 확인
for s in sentence :
    try :
        tmp = int(s) #int 함수를 썼을 때 오류가 발생하면 문자이므로 try_except 사용
        num.append(tmp) # 숫자는 num 리스트에 append
    except: #문자열이면 string 리스트에 append
        string.append(s)

#문자열은 정렬 후 join 함수를 통해 합쳐주고, 숫자열은 덧셈후 문자열로 다시 바꿔 나머지 문자열 뒤에 넣어줌
res = ''.join(sorted(string))+str(sum(num))

print(res)

# 교재 정답
# data=input()
# result=[]
# value=0
#
# for x in data:
#     if x.isalpha():
#         result.append(x)
#     else :
#         value += int(x)
#
# result.sort()
#
# if value != 0 :
#     result.append(str(value))
# print(''.join(result))