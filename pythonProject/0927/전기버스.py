import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# BACK-TRACKING

def dfs(n, cnts, B):
    global ans

    # 가지치기
    if ans <= cnts:
        return

    # 종료조건
    if n == N:
        ans = min(ans, cnts)
        return

    # 최솟값을 찾는 문제이므로
    # 교체하지 않는 경우를 먼저 호출해야 실행시간 감소!

    # 교체하지 않는 경우
    if B > 0:  # 배터리가 남아있을 때
        dfs(n + 1, cnts, B - 1)

    # 교체하는 경우
    dfs(n+1, cnts+1, lst[n]-1)

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]

    ans = N-1   # 초깃값 : 모든 위치에서 교환
    dfs(2, 0, lst[1] - 1)       # 시작, 카운팅, 첫 번째 위치에서 이동하고 남은 배터리

    print(f'#{tc} {ans}')