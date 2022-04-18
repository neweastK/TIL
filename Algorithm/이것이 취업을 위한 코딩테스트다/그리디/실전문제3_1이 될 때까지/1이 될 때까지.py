N,K = 17, 4
cnt=0
while N!=1 :
    if N<K:
        break

    if N%K: #N이 K의 배수가 아니면
        cnt += N-(N//K)*K
        N = (N//K)*K
    else :
        N /= K
        cnt+=1
if N<K :
    cnt+=N-1
print(cnt)
