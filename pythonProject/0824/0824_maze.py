import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def bfs(i, j, N):
    vstd = [[0] * (N + 1) for _ in range(N+1)]
    Q = []

    Q.append([i, j])
    vstd[i][j] = 1

    while Q:
        i, j = Q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[1,0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # 인덱스 범위 내 위치, 벽이 아닐 때, 방문한 적 없을 때
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and vstd[ni][nj] == 0:
                Q.append([ni, nj])
                vstd[ni][nj] = 1

    return 0



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # start index 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break

    print(f'#{test_case} {bfs(i, j, N)}')