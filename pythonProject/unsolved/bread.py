import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 'Possible'
    cnt = 0  # 도착한 사람수
    lst.sort()

    for t in lst:
        cnt += 1
        if cnt > t // M * K:  # 현재 도착한 사람수보다 붕어빵 개수가 적다면: impossible
            ans = 'Impossible'
            break

    print(f'#{test_case} {ans}')





