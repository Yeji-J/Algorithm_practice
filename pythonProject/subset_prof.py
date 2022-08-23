import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# -- Algorithm Process --
# 가능한 모든 경우를 다 탐색하고
# 시간을 줄이고 싶을 때
# 종료 조건 위에서 가지치기

def dfs(n, sm):
    global ans

    # 가지치기는 젤 위에서, 젤 마지막 순서
    if sm > K:      # 이미 K를 초과했을 때
        return

    # 종료조건
    if n == N:
        if sm == K:
            ans += 1
        return

    # dfs(n+1) 호출
    dfs(n+1, sm+lst[n]) # 사용하는 경우
    dfs(n+1, sm)        # 사용하지 않는 경우



T = int(input())
for test_case in range(1, T+1):
    T = int(input())
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    dfs(0, 0)