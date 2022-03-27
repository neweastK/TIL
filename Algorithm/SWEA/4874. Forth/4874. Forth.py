T= int(input())

for tc in range(T):
    formula = input().split()
    stack = []

    for i in formula :
        if i == "." :
            if len(stack) == 1 :
                result = stack[0]
            else :
                result = "error"

        elif i in ["+","*","-","/"] :
            if len(stack) < 2 :
                result = "error"
                break

            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if i == "+" :
                res = num1 + num2
            elif i == "-" :
                res = num1 - num2
            elif i == "/" :
                res = num1 // num2
            else:
                res = num1 * num2
            stack.append(res)
        else :
            stack.append(i)

    print(f'#{tc+1} {result}')