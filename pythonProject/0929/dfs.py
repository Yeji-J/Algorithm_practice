import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def dfs(N):
    vstd[N] = 1
    ans.append(N)

    for nxtN in adj[N]:
        if not vstd[nxtN]:
            dfs(nxtN)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[]*E for _ in range(E)]

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # 크기가 작은 순서대로 방문
    for lst in adj:
        lst.sort()

    vstd = [0] * E
    ans = []
    dfs(1)

    print(f'#{tc}', *ans)


