changers = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()
cnt = 0
for changer in changers:
    cnt += word.count(changer)
    word = word.replace(changer,'.')

word = word.replace('.','')
res = cnt+len(word)
print(res)