import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def escape(i, j):
    visited = [[0] * N for _ in range(N)]  # 방문 표시
    Q = []

    Q.append([i, j])          # 출발지 추가
    visited[i][j] = 1         # 시작점 표시(처리 우선순위 표시)
                            # 처리 우선순위 == 연결된 간선 수

    while Q:
        i, j = Q.pop(0)                     # Q pop 출발지 설정

        if maze[i][j] == 3:                 # 도착이면
            return visited[i][j] - 2        # 출발지 & 도착지 빼서 리턴

        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:       # 상하좌우 탐색
            ni, nj = i + di, j + dj

            # 인덱스 범위 안 + 벽이 아니고 + 방문한 적 없는 곳이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                Q.append([ni, nj])                      # Q에 추가
                visited[ni][nj] = visited[i][j] + 1     # 처리 우선순위 표시(방문 표시)


    return 0        # 길이 없으면 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j               # 출발지
                break

    print(f'#{test_case} {escape(si, sj)}')