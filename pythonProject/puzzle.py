import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnts = 0

    for i in range(N):
        sm = 0
        for j in range(N-K+1):
            for _ in range(K):
                sm += puzzle[i][j]
                j += 1
        if sm >= 3:
            cnts += 1

    print(cnts)