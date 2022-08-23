import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# typical back-tracking
def bTrack(n, sm):
    global ans
    if sm >= ans:       # 여태까지의 합이 이미 ans보다 크거나 같은경우 가지치기
        return

    if n == N:
        if ans > sm:
            ans = sm
            return

    for j in range(N):
        if not vstd[j]:
            vstd[j] = 1
            bTrack(n+1, sm+arr[n][j])
            vstd[j] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vstd = [0] * N  # 열 인덱스 체크
    ans = 10 * N
    bTrack(0, 0) # n == 0 (0행), sum = 0

    print(f'#{test_case} {ans}')