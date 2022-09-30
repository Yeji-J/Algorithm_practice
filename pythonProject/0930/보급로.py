import sys
sys.stdin = open("input.txt", "r")

INF = 1000000
def go(si, sj):
    q = []
    q.append((si,sj))
    s[si][sj] = arr[si][sj]

    while q:
        si, sj = q.pop(0)
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and s[ni][nj] > s[si][sj]+arr[ni][nj]:
                q.append((ni, nj))
                s[ni][nj] = s[si][sj]+arr[ni][nj]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    s = [[INF]*N for _ in range(N)]

    ans = 0
    go(0, 0)

    print(f'#{tc} {s[N-1][N-1]}')