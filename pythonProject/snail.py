import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = j = dr = 0
    cnt = 1
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N * N:
        ni, nj = i + di[dr], j + dj[dr]  # 이동할 좌표계산
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:  # 기록가능: 범위내이고 0이면
            i, j = ni, nj  # 현재좌표 이동
            arr[i][j] = cnt
            cnt += 1
        else:  # 불가능 => 방향전환후 기록
            dr = (dr + 1) % 4

    print(f'#{test_case}')
    for lst in arr:
        print(*lst)