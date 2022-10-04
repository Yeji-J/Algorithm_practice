import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

# 0은 통로, 1은 벽, 2는 출발, 3은 도착

def escape(si, sj):
    stk = []
    vstd[si][sj] = 1 # 방문 표시

    while True:
        # 벽이 아니면 가는 조건 => 2, 3도 가야하니까 & 도착점을 못 갈 수도 있으니까
        for di, dj in scan:
            ni, nj = (si + di), (sj + dj)
            if 0 <= ni < N and 0 <= nj < N and not vstd[ni][nj] and maze[ni][nj] != 1:
                stk.append([si, sj])    # 지금 기준점을 탐색해야 하기 때문에
                si, sj = ni, nj # 기준점이 바뀌고
                vstd[ni][nj] = 1 # ni, nj 방문표시
                break
        else:
            if stk:
                si, sj = stk.pop()
            else:
                break


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

    vstd = [[0]*N for _ in range(N)]    # 방문한 곳
    escape(si, sj)

    print(f'#{test_case} {vstd[ei][ej]}')   # 목적지가 방문 됐는지 안 됐는지 출력



