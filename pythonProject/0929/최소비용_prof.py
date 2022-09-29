import sys
sys.stdin = open("input.txt", "r")

INF = 100 * 100 * 10        # N * N * 값
def bfs(si, sj):
    q = []
    s = [[INF]*N for _ in range(N)]

    q.append([si,sj])
    s[si][sj] = 0       # arr[si][sj] 값 할당

    while q:
        ci, cj = q.pop(0)       # 중복 방문 가능 : q empty까지 방문
        for di, dj in ((0,1), (1,0), (-1,0), (0,-1)):
            ni, nj = ci+di, cj+dj
            # 범위 내에 있고, 다음위치 > 현재위치 + 다음위치 비용
            if 0 <= ni < N and 0 <= nj < N and s[ni][nj] > s[ci][cj] + 1 + max(0, arr[ni][nj] - arr[ci][cj]):
                s[ni][nj] = s[ci][cj] + 1 + max(0, arr[ni][nj] - arr[ci][cj])
                q.append([ni,nj])

    return s[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {bfs(0,0)}')
