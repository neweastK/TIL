T = int(input())

for tc in range(T):
    sentence = input()
    stack = [0] #스택이 아무것도 없을 때 해결법

    for s in sentence :
        tmp = stack[-1]
        if s == tmp : #만약 stack의 맨 끝이 같은 문자면
            stack.pop()
        else : # 다르면 그 문자를 추가해준다
            stack.append(s)

    print(f'#{tc+1} {len(stack)-1}')

