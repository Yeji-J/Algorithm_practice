import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

C, R = map(int, input().split())
N = int(input())
hall = [[0] * R for _ in range(C)]

di = [0, -1, 0, 1]      # i 오 -> 아래 -> 왼 -> 위
dj = [1, 0, -1, 0]      # j 오 -> 아래 -> 왼 -> 위

i, j = 0, 0      # i, j : 시작 위치
dr = 0              # dr : 방향
cnt = 1             # 대기 순서

hall[i][j] = cnt     # 처음 배정받은 사람 시작
cnt += 1

if N > C * R:
    ans = [0]
else:
    while cnt <= N:         # 해당 좌석 배정까지
        ni, nj = i + di[dr], j + dj[dr]     # 이동할 좌표

        # 범위 내, 안 가본 곳
        if 0 <= ni < C and 0 <= nj < R and hall[ni][nj] == 0:
            i, j = ni, nj  # 좌표 이동
            hall[i][j] = cnt      # 방문
            cnt += 1

        else:       # 불가능 => 방향 전환
            dr = (dr + 1) % 4

    ans = [i+1, j+1]

print(*ans)

