import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def bfs(s):
    q = []
    q.append((s, 0))

    while q:
        s, res = q.pop(0)

        if s == M:
            return res






T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bfs(N)
