import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def minSum(i, j, sm):
    global ans
    # 가지치기
    if sm > ans:
        return
    
    # 종료조건
    if i == N-1 and j == N-1:
        if ans > sm:
            ans = sm
        return

    # 오른쪽
    di, dj = i, j + 1
    if 0 <= di < N and 0 <= dj < N:
        minSum(di, dj, sm+arr[di][dj])

    # 아래
    ni, nj = i + 1, j
    if 0 <= ni < N and 0 <= nj < N:
        minSum(ni, nj, sm+arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N
    minSum(0, 0, arr[0][0])

    print(f'#{tc} {ans}')