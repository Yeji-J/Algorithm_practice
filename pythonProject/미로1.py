import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def escape(i, j):
    visited = [[0] * 16 for _ in range(16)]     # 방문 표시
    Q = []

    Q.append([i, j])    # 출발
    visited[i][j] = 1   # 출발지 표시

    while Q:
        i, j = Q.pop(0)
        if maze[i][j] == 3:     # 도착했다면 return 1
            return 1

        # 사방 탐색
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # 벽이 아니고 방문한 적 없다면 (사방이 벽임)
            if maze[ni][nj] != 1 and not visited[ni][nj]:
                Q.append([ni, nj])          # 큐에 추가
                visited[ni][nj] = 1         # 방문으로 표시

    return 0        # 다 돌아도 길이 없다면


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 출발지 & 도착지
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j

    print(f'#{tc} {escape(si, sj)}')
