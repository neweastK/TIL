# import sys
# sys.setrecursionlimit(10**7)
#
# def dfs(sentence,word) :
#     global stack
#     global ans
#
#
#     if len(stack) == 0 :
#         ans = sentence
#         return
#
#
#     else :
#         sentence = [stack.pop()] + sentence
#         if sentence[0:len(word)] == word :
#             del sentence[0:len(word)]
#         dfs(sentence,word)
#
# stack = [x for x in input()]
# bomb = [x for x in input()]
# ans=""
# dfs([stack.pop()],bomb)
# if len(ans) == 0 :
#     print('FURLA')
# else :
#     print("".join(ans))


stack = [x for x in input()]
bomb = [x for x in input()]
sentence=[]

while stack :
    if len(stack) < len(bomb):
        sentence=stack+sentence
        break

    sentence = [stack.pop()] + sentence
    if sentence[0:len(bomb)] == bomb:
        del sentence[0:len(bomb)]

if len(sentence) == 0 :
    print('FURLA')
else :
    print("".join(sentence))
