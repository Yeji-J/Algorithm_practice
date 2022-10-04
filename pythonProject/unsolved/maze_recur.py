import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def escape(si, sj):
    vstd[si][sj] = 1 # 방문 표시

    while True:
        # 벽이 아니면 가는 조건 => 2, 3도 가야하니까 & 도착점을 못 갈 수도 있으니까
        for di, dj in scan:
            ni, nj = (si + di), (sj + dj)
            if 0 <= ni < N and 0 <= nj < N and not vstd[ni][nj] and maze[ni][nj] != 1:
                vstd[ni][nj] = 1 # ni, nj 방문표시
                escape(ni, nj)






T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    scan = [(0, -1), (0, 1), (-1, 0), (1, 0)]       # 좌우상하 인덱스

    # 출발지, 목적지
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
            elif maze[i][j] == 3:
                ei, ej = i, j
    vstd = [[0] * N for _ in range(N)]
    escape(si, sj)

    print(f'#{test_case} {vstd[ei][ej]}')