import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def bfs(v, N):     # v 시작 N 마지막
    vstd = [0] * (N+1)
    q = []
    q.append(v)
    vstd[v] = 1
    while q:                # 큐가 비어있지 않으면
        v = q.pop(0)        # 디큐
        print(v, end=' ')
        for w in arr[v]:    # 인접한 정점에 대해
            if vstd[w] == 0:    # 방문하지 않았다면
                q.append(w)     # q에 추가
                vstd[w] = v + 1     # 처리 우선순위
    return

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    arr = [[] for _ in range(N)]
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i].append(j)
        arr[j].append(i)

    print(f'#{test_case} {(bfs(1, N))}')
