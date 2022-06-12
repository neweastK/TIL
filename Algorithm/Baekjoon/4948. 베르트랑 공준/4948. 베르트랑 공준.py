import sys

# 소수 판별 함수
def checking(number):
    # 반복을 줄이기 위해 루트값까지만 확인
    # (약수는 짝으로 이루어져있기 때문에 루트값 이전까지 약수가 없다면 그 이후로도 없음)
    for i in range(1,int(number**0.5)+1):
        if i == 1:
            continue
        if number % i == 0:
            return False
    else:
        return True

# 시간 초과를 막기 위해 입력값을 한번에 받는다
numbers = []
while True :
    N = int(sys.stdin.readline())
    # 입력값이 0이면 중단
    if N == 0 :
        break
    else :
        numbers.append(N)

# 소수를 담을 리스트
primes = []
# 입력값 중 가장 작은 값부터 가장 큰값의 2배까지를 범위로 지정하여 소수를 구한다
maximum_number = max(numbers)
minimum_number = min(numbers)
for number in range(minimum_number,2*maximum_number+1):
    if checking(number) and number!=1:
        primes.append(number)

# 입력값을 돌면서 해당 입력값부터 입력값의 두배까지 범위에 속하는 소수가 몇개인지 센다
for num in numbers :
    cnt = 0
    for i in range(len(primes)):
        if num<primes[i]<=2*num :
            cnt+=1
    print(cnt)