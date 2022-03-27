# sentence = "print('{} {}'.format(1, 2))"
def check_bracket(sentence):
    stack = []
    for w in sentence:
        if w in bracket.keys():  # 글자가 여는괄호라면
            stack.append(w)  # 스택에 넣어주고
        elif w in bracket.values():  # 닫는 괄호라면
            if len(stack) > 0:
                tmp = stack.pop()  # pop(여는괄호를 꺼내서)해서 비교해준다
                if bracket[tmp] != w :
                    return 0
            else:  # 닫는 괄호를 만났는데 스택이 비어있다면 이미 틀린 것
                return 0

    else:
        if len(stack)>0 :# 문장을 다 돌았는데 stack에 무언가 남아있다면 실패
            return 0
        else :
            return 1

T = int(input())

bracket = {"(": ")", "{": "}"}
for tc in range(T):
    sentence = input()
    result = check_bracket(sentence)
    print(f'#{tc+1} {result}')

