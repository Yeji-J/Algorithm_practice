import sys
sys.stdin = open("input.txt", "r")

# 가능한 모든 경우 (연산자 카드가 있는 경우)

def dfs(n, num, add, sub, mul, div):         # 연산자 개수 넘겨주기
    global mx, mn

    if n == N:
        mx = max(num, mx)
        mn = min(num, mn)
        return

    if add:
        dfs(n+1, num + lst[n], add-1, sub, mul, div)
    if sub:
        dfs(n+1, num - lst[n], add, sub-1, mul, div)
    if mul:
        dfs(n+1, num * lst[n], add, sub, mul-1, div)
    if div:
        # //는 음수의 경우 몫 -1.xx가 몫 -2가 되기 때문에
        # / 나누기를 하고 int()로 정수형 변환을 해줘야 함 !
        dfs(n+1, int(num/lst[n]), add, sub, mul, div-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    lst = list(map(int, input().split()))

    mn = int(1e8)        # == int(100000000.0)      float값이기 때문에 int로 바꿔줘 ~
    mx = int(-1e8)

    dfs(1, lst[0], add, sub, mul, div)

    print(f'#{tc} {mx-mn}')