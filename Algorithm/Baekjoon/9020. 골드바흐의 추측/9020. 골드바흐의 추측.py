import sys

# 골드바흐 파티션 출력하는 함수
def gold(target_number):
    # 소수인지 판별하는 함수
    def checking(number):
        for i in range(1, int(number ** 0.5) + 1):
            if i == 1:
                continue
            if number % i == 0:
                return False
        else:
            return True
    # 어차피 입력값은 모두 짝수이기 때문에 2로 나눈 숫자부터 시작해도 문제 없음
    a = int(target_number // 2)
    b = int(target_number // 2)
    while True:
        # 두 수가 모두 소수인 경우를 찾는다
        if checking(a) and checking(b):
            return [a, b]
        # 아닌 경우, a는 -1, b는 +1 해준다
        else:
            a -= 1
            b += 1

T = int(sys.stdin.readline())

for tc in range(T):
    number = int(sys.stdin.readline())
    ans = gold(number)
    print(*ans)
