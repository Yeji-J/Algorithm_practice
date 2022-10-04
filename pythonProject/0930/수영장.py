import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans
    if sm >= ans:
        return

    if n > 12:
        ans = min(sm, ans)
        return

    # D1
    dfs(n+1, sm + lst[n]*D1)
    # M1
    dfs(n+1, sm + M1)
    # M3
    dfs(n+3, sm + M3)
    # Y1
    dfs(n+12, sm + Y1)

T = int(input())
for tc in range(1, T+1):
    D1, M1, M3, Y1 = list(map(int, input().split()))
    lst = [0] + list(map(int, input().split()))     # n월부터 사용하려고 앞에 [0] 붙이기

    ans = 3000 * 12
    dfs(1, 0)       # n월, 이용권 금액 누적
    print(f'#{tc} {ans}')


