from collections import deque
import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# 3차원 BFS
# 상 하 좌 우 위 아래
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, sys.stdin.readline().split())
B = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

q = deque()
# 3차원으로 훑어서 익은 토마토 위치 담기
for z in range(H):          # 높이(박스 개수)
    for x in range(N):
        for y in range(M):
            if B[z][x][y] == 1:
                q.append((z, x, y, 0))
cnts = -1
while q:    # 익은 토마토 모두 BFS 적용할 때까지
    z, x, y, cnts = q.popleft()
    # if cnts < B[z][x][y]:
    #     cnts = B[z][x][y]

    for d in range(6):
        nz, nx, ny = z+dz[d], x+dx[d], y+dy[d]
        # 모든 인덱스가 범위 내에 있고, 안 익은 토마토면
        if 0 <= ny < M and 0 <= nx < N and 0 <= nz < H and not B[nz][nx][ny]:
            q.append((nz, nx, ny, cnts+1))
            B[nz][nx][ny] = 1
            # B[nz][nx][ny] = B[z][x][y] + 1  # 일수 + 1

for box in B:
    for tmt in box:
        if 0 in tmt:        # 익힐 수 없는 토마토가 있으면
            cnts = -1
            break
    if cnts == -1:
        break

print(cnts)


# # 토마토가 전부 익었는지 확인
# def check(box):
#     for lst in box:
#         if 0 in lst:                # 안 익은게 있으면 False
#             return False
#     return True                 # 다 익었으면 True
#
# def bfs(si, sj, n):
#     global cnts
#
#     # 종료조건
#     if check(boxes[n]):
#         return
#
#     for di, dj in ((0,-1), (-1,0), (1,0), (0,-1)):
#         ni, nj = si+di, sj+dj
#         if 0 <= ni < M and 0 <= nj < N and boxes[n][ni][nj] == 0:
#             cnts += 1
#             boxes[n][ni][nj] = 1
#             bfs(ni, nj, n)
#
#     # 위에 있는 box
#     if 0 < n < H and boxes[n-1][si][sj] == 0:
#         cnts += 1
#         bfs(si, sj, n-1)
#
#     # 아래 있는 box
#     if 0 <= n < H-1 and boxes[n+1][si][sj] == 0:
#         cnts += 1
#         bfs(si, sj, n+1)
#
#
#
# N, M, H = map(int, input().split())
# boxes = []
# for _ in range(H):
#     box = [list(map(int, input().split())) for _ in range(M)]
#     boxes.append(box)
#
# # -1 없음 0 안익음 1 익음
# cnts = 0
# for box in boxes:
#     if check(box):
#         continue
#     else:
#         for n in range(H):
#             for i in range(M):
#                 for j in range(N):
#                     if boxes[n][i][j]:
#                         bfs(i, j, 0)
#
# print(cnts)