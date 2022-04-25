s = "xababcdcdababcdcd"
x=1
answer = 9999
while x <= len(s)//2+1 :
    cut_strs = [s[i:i+x] for i in range(0,len(s),x)]
    tmp = cut_strs[0]
    cnt=1
    res=""
    for cut_str in cut_strs[1:] :
        if cut_str == tmp :
            cnt+=1
        else :
            res += tmp if cnt==1 else str(cnt)+tmp
            tmp = cut_str
            cnt=1
    res += tmp if cnt == 1 else str(cnt) + tmp

    if len(res) < answer :
        answer = len(res)
    x+=1

print(answer)