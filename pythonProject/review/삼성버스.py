import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    cnts = [0] * P

    print(lines)
    print(stops)


