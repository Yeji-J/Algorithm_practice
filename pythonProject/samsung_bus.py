import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lines = []
    for _ in range(N):
        lines.append(list(map(int, input().split())))
    P = int(input())
    stops = []
    cnts = [0] * P
    for _ in range(P):
        stops.append(int(input()))

    for idx in range(N):
        lst = []
        for k in range(lines[idx][0], lines[idx][1]+1):
            lst.append(k)
        for stop in range(P):
            if stops[stop] in lst:
                cnts[stop] += 1

    print(f'#{test_case}', *cnts)