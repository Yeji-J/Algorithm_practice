import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def bfs(si, sj):
    q = []
    ans = []

    # 시작
    q.append((si, sj))
    v[si][sj] = 1
    ans.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위 내 + 방문 안 한 곳 + 나와 1 차이
            # abs: 굳이 낮은 시작점 찾지 않아도 1차이로 연결된 곳이면 카운트하려고
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and abs(arr[ci][cj]-arr[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                ans.append(arr[ni][nj])

    return len(ans), min(ans)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt, num = 0, N*N
    # 전체순회: 방문하지 않은 노드 방문
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                tcnt, tnum = bfs(i, j)
                # tcnt 더 클 때 or 같지만 num이 더 작을 때 갱신
                if cnt < tcnt or cnt == tcnt and tnum < num:
                    cnt, num = tcnt, tnum

    print(f'#{tc} {num} {cnt}')