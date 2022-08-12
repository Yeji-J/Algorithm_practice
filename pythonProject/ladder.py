import sys
sys.stdin = open("input.txt", "r")

T = 3
for test_case in range(1, T+1):
    N = 100
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    i, j = N-1, 9
    for tj in range(N):
        if arr[i][tj] == 2:
            j = tj
            break

    while i > 0:
        if j > 0 and arr[i][j-1] == 1:
            arr[i][j] = 0
            j -= 1
        elif j < 99 and arr[i][j+1] == 1:
            arr[i][j] = 0
            j += 1
        else:
            i -= 1

    print(f'#{test_case} {j}')
