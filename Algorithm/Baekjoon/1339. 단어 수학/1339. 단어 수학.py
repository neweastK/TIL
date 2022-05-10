N = int(input())

# 글자의 실제 자리수를 표시할 리스트
word_loc = {}

for _ in range(N):
    word = input()

    for idx,value in enumerate(word[::-1]) :
        if value in word_loc :
            word_loc[value] += 10**idx
        else :
            word_loc[value] = 10**idx

results = list(word_loc.items())
print(results)
results.sort(key=lambda x : -x[1])

sum = 0
num = 9
for result in results :
    sum += result[1]*num
    num -= 1
print(results)
print(sum)

