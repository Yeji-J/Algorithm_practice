import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def bfs(i, j, N):
    vstd = [[0]*N for _ in range(N)]
    q = []
    q.append([i, j])
    vstd[i][j] = 1 # 시작점 표시
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and vstd[ni][nj] == 0:     # 벽이 아니고 방문한 적 없으면
                q.append([ni, nj])
                vstd[ni][nj] = vstd[i][j] + 1

    return 0        # 못 찾았을 때

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break



    print(f'#{test_case} {bfs(sti, stj, N)}')