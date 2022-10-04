import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(N, cnts):
    q = deque()             # 큐 생성
    q.append((N, cnts))       # 초기값
    v[N] = 1                # 방문표시

    while q:
        R, C = q.popleft()
        if R == M:
            return C

        for i in range(4):
            if i == 0:
                if 1 <= R+1 <= INF and not v[R+1]:
                    q.append((R+1, C+1))
                    v[R+1] = 1

            elif i == 1:
                if 1 <= R-1 <= INF and not v[R-1]:
                    q.append((R-1, C+1))
                    v[R-1] = 1

            elif i == 2:
                if 1 <= R*2 <= INF and not v[R*2]:
                    q.append((R*2, C+1))
                    v[R*2] = 1

            else:
                if 1 <= R-10 <= INF and not v[R-10]:
                    q.append((R-10, C+1))
                    v[R-10] = 1

INF = 1000000
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    v = [0] * (INF+1)

    print(f'#{tc} {bfs(N, 0)}')

