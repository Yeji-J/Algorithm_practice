import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# def check(si, sj):
#     # 위
#     for i in range(si):
#         if arr[i][sj]:
#             return
#
#     # 좌측위 대각선
#     i, j = si-1, sj-1
#     while i >= 0 and j >= 0:
#         if arr[i][j]:
#             return
#         else:
#             i -= 1
#             j -= 1
#
#     # 우측위 대각선
#     i, j = si-1, sj+1
#     while i >= 0 and j < N:
#         if arr[i][j]:
#             return
#         else:
#             i -= 1
#             j += 1
#
#     return 1
#
# def dfs(n):
#     global cnts
#
#     if n == N:
#         cnts += 1
#         return
#
#     for j in range(N):              # 0 -> N-1
#         if check(n, j):             # 놓는거 가능?
#             arr[n][j] = 1
#             dfs(n+1)                # 다음행
#             arr[n][j] = 0

def dfs_tbl(n):
    global cnts

    if n == N:
        cnts += 1
        return

    for j in range(N):
        if j not in v1 and (n+j) not in v2 and (n-j) not in v3:         # 열, 대각선 겹치지 않게 (index 규칙에 따라)
            v1.append(j), v2.append(n+j), v3.append(n-j)
            dfs_tbl(n+1)
            v1.pop(), v2.pop(), v3.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    v1 = []
    v2 = []
    v3 = []
    cnts = 0
    dfs_tbl(0)
    # dfs(0)  # 행
    print(f'#{tc} {cnts}')