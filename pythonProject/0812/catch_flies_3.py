import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cross = []
    x = []

    for k in range(1, M):
        cross += [[-k, 0], [k, 0], [0, -k], [0, k]]

    for l in range(1, M):
        x += [[-l, l], [l, -l], [l, l], [-l, -l]]

    flies = 0
    for i in  range(N):
        for j in range(N):
            sm1 = arr[i][j]
            for di, dj in cross:
                di = i + di
                dj = j + dj
                if 0 <= di < N and 0 <= dj < N:
                    sm1 += arr[di][dj]
            if sm1 > flies:
                flies = sm1

            sm2 = arr[i][j]
            for ni, nj in x:
                ni = i + ni
                nj = j + nj
                if 0 <= ni < N and 0 <= nj < N:
                    sm2 += arr[ni][nj]
            if sm2 > flies:
                flies = sm2

    print(f'#{test_case} {flies}')
