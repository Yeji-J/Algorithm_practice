import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    smMin = 10000 * M
    smMax = 0

    for i in range(N-M+1):
        sm = 0
        for j in range(i, i+M):
            sm += arr[j]

        if sm > smMax:
            smMax = sm
        if sm < smMin:
            smMin = sm

    print(f'#{test_case} {smMax - smMin}')
