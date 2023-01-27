formula = input()

tmp = []
nums = ''
bracket = True
for i in formula:
    if i == "-":
        tmp.append(str(int(nums)))
        nums = ''
        if bracket:
            tmp.append(i)
            tmp.append("(")
            bracket = not(bracket)
        else:
            tmp.append(")")
            tmp.append(i)
            tmp.append("(")

    elif i == "+":
        tmp.append(str(int(nums)))
        nums = ''
        tmp.append(i)
    else:
        nums+=i

tmp.append(str(int(nums)))
if bracket == False:
    tmp.append(")")
print(eval(''.join(tmp)))




