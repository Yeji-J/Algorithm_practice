import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def minP(n, sm):
    global ans

    if sm > ans:
        return

    if n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        if not v[j]:
            v[j] = 1
            minP(n+1, sm+arr[n][j])
            v[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * N
    v = [0] * N
    minP(0, 0)

    print(f'#{tc} {ans}')