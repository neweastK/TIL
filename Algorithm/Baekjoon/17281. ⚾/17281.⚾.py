# import sys
# from itertools import permutations
# input = sys.stdin.readline
#
#
# # def make_lineup(score_boards):
# #     # 2번타자부터 9번 타자
# #     players = list(range(1, 9))
# #     orders = []
# #     # 선수들 중 1~3번 타자 라인업 구성
# #     table_setter = list(permutations(players, 3))
# #     for setter in table_setter:
# #         # 선수들 중 5~9번 타자 라인업 구성
# #         # 테이블세터로 구성된 선수들 빼고 나머지 선수들 타순 짜기
# #         lower_line_players = list(set(players) - set(setter))
# #         lower_line = list(permutations(lower_line_players, 5))
# #
# #         # 모든 라인업 경우의 수 확인하기
# #         for l in lower_line:
# #             lineup = list(setter) + [0] + list(l)
# #
# #             # lineup은 나올 수 있는 하나의 타순. 그 타순일 때 이닝별 타자들의 결과
# #             each_lineup_total_result = []
# #             for score_board in score_boards :
# #                 inning_results = tuple([score_board[line] for line in lineup])
# #                 # test는 하나의 타순으로 총 이닝동안 낼 결과물들
# #                 each_lineup_total_result.append(inning_results)
# #             # orders에는 만들 수 있는 모든 타순으로 총 이닝동안 낼 수 있는 결과물들
# #             orders.append(tuple(each_lineup_total_result))
# #
# #             #예시) orders = [[[0번째타순으로 1이닝에 낼 결과물],[0번째 타순으로 2이닝에 낼 결과물]],[[1번째 타순으로 1이닝에 낼 결과물],[1번째 타순으로 2이닝에 낼 결과물]]...]
# #
# #     return orders
#
#
# def make_lineup(score_boards):
#     # 2번타자부터 9번 타자
#     players = list(range(1, 9))
#     orders = []
#     # 선수들 중 1~3번 타자 라인업 구성
#     line_up = list(permutations(players, 8))
#     for l in line_up :
#         lineup = list(l)[:3] + [0] + list(l)[3:]
#         # lineup은 나올 수 있는 하나의 타순. 그 타순일 때 이닝별 타자들의 결과
#         each_lineup_total_result = []
#         for score_board in score_boards :
#             inning_results = tuple([score_board[line] for line in lineup])
#             # test는 하나의 타순으로 총 이닝동안 낼 결과물들
#             each_lineup_total_result.append(inning_results)
#         # orders에는 만들 수 있는 모든 타순으로 총 이닝동안 낼 수 있는 결과물들
#         orders.append(tuple(each_lineup_total_result))
#
#             #예시) orders = [[[0번째타순으로 1이닝에 낼 결과물],[0번째 타순으로 2이닝에 낼 결과물]],[[1번째 타순으로 1이닝에 낼 결과물],[1번째 타순으로 2이닝에 낼 결과물]]...]
#     return orders
#
#
# T = int(input())
# score_boards = []
# for t in range(T):
#     score_boards.append(list(map(int,input().split())))
#
# results = make_lineup(score_boards)
# print(len(set(results)))
# answer = 0
# # 각 타순별로 점수 세는 것
# for result in set(results) :
#     point = 0
#     base = [False]*3
#     # 각 이닝별 점수 세기
#     k = -1
#     for res in result:
#         out_cnt = 0
#         # 각 타자별 결과 :
#         while True :
#             if k == 8 :
#                 k = 0
#             else :
#                 k += 1
#             tmp = res[k]
#             if tmp == 0 :
#                 out_cnt += 1
#                 if out_cnt == 3 :
#                     base=[False]*3
#                     break
#             elif tmp == 4 :
#                 point += (base.count(True)+1)
#                 base = [False]*3
#             else :
#                 # 안타이기 때문에 진루
#                 for b in range(2,-1,-1):
#                     # 만약 베이스에 주자가 있다면
#                     if base[b] :
#                         # 주자 이동시키기
#                         base[b] = False
#                         # 만약 목적지가 홈을 넘어섰다면 득점 처리
#                         if (tmp+b) >= 3 :
#                             point += 1
#                         # 그게 아니면 다음 베이스로 이동시키기
#                         else :
#                             base[b+tmp] = True
#                 # 타자 이동
#                 base[tmp-1] = True
#     # 주어진 이닝이 끝나면 다음 타순 후보로 넘어감
#     else :
#         if answer < point :
#             answer = point
#
# print(answer)
#
#
# #
# # # 하나의 타순
# # i = 0
# # res = 0
# # point = 0
# #
# # # 각 타순을 돌면서 점수 계산해보기
# # for order in orders :
# #     point = 0
# #     out_cnt = 0
# #     base = [False] * 3
# #     inning = 0
# #     k = -1
# #     while True :
# #         score = scores[inning]
# #         if k == 8 :
# #             k = 0
# #         else :
# #             k+=1
# #         # 하나의 타자가 타석에서 낸 결과 tmp
# #         tmp = score[order[k]]
# #         # out 이면
# #         if tmp == 0 :
# #             # 아웃카운트 증가
# #             out_cnt+=1
# #             # 만약 쓰리 아웃이면
# #             if out_cnt == 3:
# #                 # 이닝 증가
# #                 inning += 1
# #                 # 주어진 이닝이 다 지났을 경우
# #                 if inning >= T :
# #                     # 얻을 수 있는 점수의 최댓값 구하기
# #                     if res < point :
# #                         res = point
# #                     # 다음 타순 후보 살펴보기
# #                     break
# #                 base=[False]*3
# #                 out_cnt=0
# #         # 만약 홈런이라면?
# #         elif tmp == 4:
# #             point += (base.count(True)+1)
# #             base = [False] * 3
# #         else :
# #             # 안타이기 때문에 진루
# #             for b in range(2,-1,-1):
# #                 # 만약 베이스에 주자가 있다면
# #                 if base[b] :
# #                     # 주자 이동시키기
# #                     base[b] = False
# #                     # 만약 목적지가 홈을 넘어섰다면 득점 처리
# #                     if (tmp+b) >= 3 :
# #                         point += 1
# #                     # 그게 아니면 다음 베이스로 이동시키기
# #                     else :
# #                         base[b+tmp] = True
# #             # 타자 이동
# #             base[tmp-1] = True
# #
# # print(res)

import sys
from itertools import permutations
input = sys.stdin.readline

T = int(input())
innings = [list(map(int,input().split())) for _ in range(T)]

def get_score(order):
    # 각 이닝별
    point = 0
    player_order = 0
    for inning in innings :
        out_cnt = 0
        b1,b2,b3 = 0,0,0
        while out_cnt<3 :
            if player_order == 9 :
                player_order = 0
            if inning[order[player_order]] == 0 :
                out_cnt += 1
            elif inning[order[player_order]] == 1 :
                point += b3
                b1,b2,b3 = 1,b1,b2
            elif inning[order[player_order]] == 2 :
                point += b2+b3
                b1,b2,b3 = 0,1,b1
            elif inning[order[player_order]] == 3 :
                point += b1+b2+b3
                b1,b2,b3 = 0,0,1
            else :
                point += (b1+b2+b3+1)
                b1,b2,b3 = 0,0,0
            player_order+=1

    return point


###################################### 1번 ################################
# 2번타자부터 9번 타자
players = list(range(1, 9))
orders = []
# 선수들 중 1~3번 타자 라인업 구성
table_setter = list(permutations(players, 3))
for setter in table_setter:
    # 선수들 중 5~9번 타자 라인업 구성
    # 테이블세터로 구성된 선수들 빼고 나머지 선수들 타순 짜기
    lower_line_players = list(set(players) - set(setter))
    lower_line = list(permutations(lower_line_players, 5))

    # 모든 라인업 경우의 수 확인하기
    for l in lower_line:
        lineup = list(setter) + [0] + list(l)
        orders.append(lineup)
ans = 0
for order in orders :
    res = get_score(order)
    if res > ans :
        ans = res

print(ans)


###################################### 2번 ################################

# 모든 타순 구하기
players = list(permutations(range(1,9),8))
ans = 0
for player in players :
    order = list(player)[:3] + [0] + list(player)[3:]
    res = get_score(order)
    if res > ans :
        ans = res

print(ans)