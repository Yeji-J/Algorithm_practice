import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def per(n, p):
    global ans

    if p <= ans:
        return

    if n == N:
        ans = max(ans, p)
        return

    for j in range(N):
        if not v[j] and arr[n][j] != 0:
            v[j] = 1
            per(n+1, p*arr[n][j]/100)
            v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(N)]

    ans = 0
    v = [0] * N
    per(0, 1)

    print(f'#{tc} {ans*100:.6f}')