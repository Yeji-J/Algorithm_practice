import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def bfs(s):
    vstd = [0] * (V + 1)
    q = []

    # 단위작업
    vstd[s] = 1
    q.append(s)
    sol.append(s)

    while q:
        s = q.pop(0)            # FIFO
        # 정답처리 필요한 경우 here

        # 안 가본 조건에 맞는 곳이면 q에 삽입
        for e in range(1, V+1):
            if e in adj[s] and not vstd[e]:
                q.append(e)
                vstd[e] = 1
                sol.append(e)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    sol = []
    bfs(1)          # 시작지점 => 방문하는 순서대로 sol에 추가

    print(f'#{test_case}', *sol)