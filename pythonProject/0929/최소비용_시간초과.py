import sys
sys.stdin = open("input.txt", "r")

def move(i, j, total):
    global minv

    if total >= minv:
        return

    if i == N-1 and j == N-1:
        minv = min(minv, total)
        return

    for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:         # 범위 내에 있고
            if arr[ni][nj] - arr[i][j] > 0:     # 높이 차가 있을 때
                move(ni, nj, total+1+(arr[ni][nj] - arr[i][j]))
            else:
                move(ni, nj, total+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [[0]*N for _ in range(N)]
    minv = 1000 * N ** 2
    v[0][0] = 1
    move(0, 0, 0)

    print(f'#{tc} {minv}')

