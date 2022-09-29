import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def dfs(n, sm):
    global ans

    # 가지치기
    if ans + B <= sm:
        return

    if n == N:
        if sm >= B and ans > sm - B:
            ans = sm - B
        return

    dfs(n+1, sm+lst[n])      # 포함하는 경우
    dfs(n+1, sm)             # 포함하지 않는 경우

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 10000 * N
    dfs(0, 0)

    print(f'#{tc} {ans}')