import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = 10
for test_case in range(1, T + 1):
    # 1 == N      2 == S
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnts = 0
    for i in range(N-1):
        for j in range(N):
            if arr[i][j] == 1 and arr[i+1][j] == 2:
                cnts += 1

    print(cnts)

