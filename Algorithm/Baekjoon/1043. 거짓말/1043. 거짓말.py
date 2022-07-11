import sys
input = sys.stdin.readline

# 사람 수, 파티 수
N,M = map(int,input().split())
second_row = input()

if len(second_row) == 2:
    print(M)
else :
    know_cnt, *know_num = map(int,second_row.split())
    # 최종 테스트를 위해 파티 참가자들을 모아둘 리스트
    final_test = []
    # 한바퀴 돌아서 진실을 아는 사람들 추출
    for _ in range(M):
        test = 0
        customer_cnt, *customers = map(int,input().split())
        final_test.append(customers)
        for i in range(customer_cnt):
            if customers[i] in know_num:
                test = 1
        else :
            if test == 1:
                know_num.extend(customers)
    # 파티 수만큼 반복해서 진실을 알게된 사람들 새로 추가
    for _ in range(M):

        # 각 파티에 참가한 사람들을 다시 순회
        for f in final_test :
            test = 0
            # 참가자들 중에서
            for customer in f :
                # 진실을 아는 사람이 있다면
                if customer in know_num :
                    test = 1
            else :
                if test == 1:
                    # 나머지 사람들도 진실을 아는 사람에 추가
                    know_num.extend(f)

    cnt = 0
    # 각 파티에 참가한 인원들을 반복문으로 순회
    for final in final_test :
        # 해당 인원이 진실을 알게된 사람들 리스트에 있다면 continue
        if set(final) & set(know_num) :
            continue
        # 아무도 진실을 모른다면 cnt 추가
        else :
            cnt+=1
    print(cnt)
