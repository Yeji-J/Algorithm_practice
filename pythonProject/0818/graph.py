import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def dfs(S, V, G):
    stk = []
    vstd = [0] * (V+1)
    vstd[S] = 1         # 시작

    while True:
        for i in range(1, V+1):
            if vstd[i] == 0 and adj[S][i] == 1:     # 방문한 적 없고, 연결된 노드
                if i == G:
                    return 1
                else:                       # G와 같지 않을 때 왔던 길 저장하고 다시 탐색
                    stk.append(S)
                    S = i
                    vstd[i] = 1
                    break
        else:                              # 막다른 길일 때
            if stk:                        # 왔던 길로 돌아가기
                S = stk.pop()
            else:
                return 0


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())    # V: 노드 E: 간선

    adj = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):                # 간선 수만큼 돌리기
        i, j = map(int, input().split())
        adj[i][j] = 1       # 다시 돌아가면 안 되기 때문에 adj[j][i]는 생략

    S, G = map(int, input().split())

    print(f'#{test_case} {dfs(S,V, G)}')





