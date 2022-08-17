import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def dfs(s):
    # [1] stack 등 필요 자료구조 초기화
    stk = []
    visited = [0] * (V+1)
    # [2] dfs 시작작업
    visited[s] = 1
    sols.append(s)

    while True:
        for e in range(1, V+1): # 1부터 7까지
            # s와 연결된, 방문 안 가본 곳
            if visited[e] == 0 and adj[s][e] == 1:
                stk.append(s)   # 돌아올 곳 push
                s = e
                visited[e] = 1
                sols.append(e)
                break   # 새로운 기준점 s부터 다시 시작
        # 현재 s 기준 방문 가능한 곳 없는 경우
        else:
            if stk:
                s = stk.pop()   # 이전으로 다시 돌아가 탐색 시작
            else:   # stack empty == dfs 탐색 끝
                break

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = adj[j][i] = 1   # 양방향으로 연결 표시

    sols = []
    dfs(1)
    print(f'#{test_case}', *sols)

