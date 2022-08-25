import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def bfs(s, e):
    visited = [0] * (V + 1)         # 방문 우선순위
    Q = []                          # 큐
    Q.append(s)
    visited[s] = 1                  # 방문 표시

    while Q:                        # 큐가 비어있지 않은 경우
        t = Q.pop(0)
        if t == e:
            return visited[e] - 1
        for i in arr[t]:            # t와 인접한 노드 중에
            if not visited[i]:      # 방문하지 않은 곳이라면
                Q.append(i)         # 큐에 추가
                visited[i] = visited[t] + 1
    return 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())        # V: 노드수 E: 간선수

    arr = [[] for _ in range(V+1)]          # 노드수만큼

    for _ in range(E):                      # 간선수만큼
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    S, G = map(int, input().split())        # S: 출발 G: 도착

    print(f'#{test_case} {bfs(S, G)}')