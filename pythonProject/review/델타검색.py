import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    sm = 0
    for i in range(N):
        for j in range(N):
            for di, dj in idx:
                di = i + di
                dj = j + dj
                if di >= 0 and dj >= 0 and di < N and dj < N:
                    d_sm = arr[di][dj] - arr[i][j]
                    if d_sm < 0:
                        sm += -d_sm
                    else:
                        sm += d_sm

    print(sm)

