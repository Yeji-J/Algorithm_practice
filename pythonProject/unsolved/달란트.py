import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T + 1):
    N, P = map(int, input().split())    # N : 달란트  P : 주머니

    num = N // P                    # 기본 값
    lst = [num] * P                 # 주머니 개수만큼의 값

    rest = N % P
    if rest:            # 나누고 남은 나머지가 있다면
        i = 0
        while rest > 0:         # 나머지가 없어질 때까지
            lst[i] += 1         # 각 값에 1씩 더해주기
            rest -= 1
            i += 1

    maxD = 1
    for D in lst:   # 모든 값 곱하기
        maxD *= D

    print(f'#{test_case} {maxD}')




