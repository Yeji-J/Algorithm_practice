import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def dfs(n, sm):
    global ans
    # 가지치기
    if ans < sm:
        return

    # 종료조건
    if n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        if not v[j]:        # 방문하지 않았다면
            v[j] = 1        # 방문 표시
            dfs(n+1, sm+arr[n][j])
            v[j] = 0        # 방문표시 해제


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N        # 최소값 (10이하 자연수)
    v = [0] * N
    dfs(0, 0)

    print(f'#{tc} {ans}')