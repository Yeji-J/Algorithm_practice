import sys
sys.stdin = open("input.txt", "r")

# 대표원소 return
def findset(v):
    while G[v] != v:
        v = G[v]
    return v

# b 대표원소에 a 대표원소 할당
def Union(a, b):
    r1 = findset(a)
    r2 = findset(b)
    G[r2] = r1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    G = [i for i in range(N+1)]

    for i in range(M):
        a, b = [lst[i*2], lst[i*2+1]]
        Union(a, b)

    # 팀 카운팅 == 자기자신이 root
    cnts = 0
    for j in range(1, N+1):
        if j == G[j]:
            cnts += 1

    print(f'#{tc} {cnts}')




