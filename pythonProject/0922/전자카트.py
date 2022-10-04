import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def admin(n, s, sm):
    global ans
    # 가지치기
    if sm > ans:
        return

    # 종료 조건
    if n == N-1:
        if ans > (sm + arr[s][0]):
            ans = sm + arr[s][0]
        return

    for i in range(1, N):
        if not v[i] and s != i:     #  방문하지 않았고 현재 위치와 다른 곳
            v[i] = 1
            admin(n+1, i, sm + arr[s][i])
            v[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 100 * N ** 2
    admin(0, 0, 0)

    print(f'#{tc} {ans}')


