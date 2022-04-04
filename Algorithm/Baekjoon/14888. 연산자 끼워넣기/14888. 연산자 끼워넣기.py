from collections import deque
import itertools

N = int(input())
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))
formula = []
for f in range(len(operators)) : # 식이 개수로 나와있으므로 순열을 위해 분리시켜준다.
    if operators[f] : # 만약 특정 연산자가 1 이상이라면
        for _ in range(operators[f]): # 그 값만큼 해당 인덱스를 빈 리스트에 넣어준다
            formula.append(f)


# 연산자로 만든 순열 (조금이라도 case를 줄이기 위해 set 사용)
perms = set(list(itertools.permutations(formula,N-1)))
res = []

# 순열을 순회하면서 작업 진행
for perm in perms :
    queue = deque(nums)
    perm = list(perm)
    operand = queue.popleft() #첫번째 피연산자 할당
    while queue : #queue 즉, 피연산자들이 다 없어질때까지
        operator = perm.pop() #연산자 할당
        operand2 = queue.popleft() #두번째 피연산자 할당
        if operator == 0 :
            tmp_res = operand+operand2
        elif operator == 1 :
            tmp_res = operand-operand2
        elif operator == 2 :
            tmp_res = operand*operand2

        else :
            # 나눗셈의 경우 음수 양수 따로 처리
            if operand < 0 or operand2 < 0 :
                tmp_res = -(abs(operand)//abs(operand2))
            else :
                tmp_res = operand//operand2
        # 첫번째 연산자에 결과를 할당해주고 다시 두번쨰 연산자와 연산 진행
        operand = tmp_res

    res.append(tmp_res)

print(max(res))
print(min(res))