import sys
sys.stdin = open("input.txt", "r")

type = {
    1:[(1,0), (0,1), (-1,0), (0,-1)],
    2:[(-1,0),(1,0)],
    3:[(0,-1),(0,1)],
    4:[(-1,0),(0,1)],
    5:[(1,0),(0,1)],
    6:[(1,0),(0,-1)],
    7:[(-1,0),(0,-1)]
}

# BFS
def guess(i, j):
    global ans
    q = [[i, j]]
    avail[i][j] = 1     # 방문표시

    while q:
        si, sj = q.pop(0)

        if avail[si][sj] == L:              # L시간 후 종료
            return

        for di, dj in type[loc[si][sj]]:                # 이동할 수 있는 다음 방향
            ni, nj = si + di, sj + dj
            # 이동하려는 좌표가 : 범위 내 + 터널이 있고 + 방문한 적 없는 곳
            if 0 <= ni < N and 0 <= nj < M and loc[ni][nj] and not avail[ni][nj]:
                # 연결되어 있을 때 : 각 좌표의 합 0
                for ti, tj in type[loc[ni][nj]]:
                    if ti + di == 0 and tj + dj == 0:
                        q.append([ni,nj])                       # q에 추가
                        avail[ni][nj] = avail[si][sj] + 1       # 이전 +1 (시간)
                        ans += 1                                # 이동 가능한 곳 +1


T = int(input())
for tc in range(1, T+1):
    # N:지도 세로, M:지도 가로, R:맨홀 세로, C:맨홀 가로, L:탈출 후 소요시간
    N, M, R, C, L = map(int, input().split())

    loc = [list(map(int, input().split())) for _ in range(N)]       # 지도
    avail = [[0]*M for _ in range(N)]                               # 탈주범 위치

    avail[R][C] = 1     # 맨홀 시작

    ans = 1
    guess(R, C)


    print(f'#{tc} {ans}')



