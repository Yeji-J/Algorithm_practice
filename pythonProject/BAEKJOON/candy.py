import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def cnt():
    for lst in arr:
        for k in range(N-1):


N = int(input())
arr = [list(str(input())) for _ in range(N)]

C = N       # 최대 먹을 수 있는 사탕

# 상하좌우 탐색
scan = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(N):
    for j in range(N):
        for di, dj in scan:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:     # 인덱스가 범위 내에 있을 때
                if arr[i][j] != arr[ni][nj]:    # 인접한 사탕과 색이 같지 않다면
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]     # 바꾸고
                    cnt()   # 사탕 수 세어보는 함수 실행