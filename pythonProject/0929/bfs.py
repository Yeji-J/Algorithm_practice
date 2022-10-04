import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def bfs():
    q = [1]     # 1부터 시작
    vstd[1] = 1

    while q:
        s = q.pop(0)
        for nxtS in adj[s]:
            if not vstd[nxtS]:
                q.append(nxtS)
                vstd[nxtS] = 1
                ans.append(nxtS)

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
    ans = [1]
    bfs()

    print(f'#{tc}', *ans)