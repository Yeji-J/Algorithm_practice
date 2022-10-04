import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def turn(num):
    idx = []
    # 해당 돌이 놓여진 인덱스 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == num:
                idx.append([i, j])

    if idx:
        for si, sj in idx:
            # 가로 세로 대각선 탐색
            scan = [[-1, 0], [-2, 0], [-1, -1], [-2, -2], [-1, 1], [-2, 2], [0, -1], [0, -2],
                    [0, 1], [0, 2], [1, 1], [2, 2], [1, -1], [2, -2], [-1, 1], [-2, 2]]

            for k in range(0, len(scan)-1, 2):
                ni, nj = si + scan[k][0], sj + scan[k][1]
                hi, hj = si + scan[k+1][0], sj + scan[k+1][1]

                # 인덱스가 범위 내에 있을 때
                if 0 <= ni < N and 0 <= nj < N and 0 <= hi < N and 0 <= hj < N:
                    # 인접한 돌이 다른색이고, 같은색 돌과 가로 or 세로 or 대각선 사이에 있을 때
                    # 자신의 돌로 만들기
                    if arr[ni][nj] != num and arr[ni][nj] != 0 and arr[hi][hj] == num:
                        arr[ni][nj] = num
                        return
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    # 초기 세팅
    arr[N//2-1][N//2-1], arr[N//2][N//2], arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1, 2, 2

    for _ in range(M):
        tmp = list(map(int, input().split()))
        arr[tmp[0]-1][tmp[1]-1] = tmp[2]
        if tmp[2] == 1:         # 흑돌일 때
            turn(1)
            print(arr)
        else:                   # 백돌일 때
            turn(2)
            print(arr)

