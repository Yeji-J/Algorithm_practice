import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(100)]
    
























    # length = 1
    # # 가로
    # M = 3
    # N = 100
    # for i in arr:
    #     j = 0
    #     print(i)
    #     while j < N-M+1:
    #         lst = i[j:j+M]
    #         if lst == lst[::-1]:
    #             length = M
    #             M += 1
    #             break
    #         else:
    #             j += 1
    #
    # print(length)