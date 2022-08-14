import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sm = 0
    for i in range(N):
        for j in range(N):
            # 앞뒤 양옆 인덱스 하나씩 대입
            for di, dj in [(-1, 0), (0, 1), (0, 1), (1, 0)]:
                di = i + di
                dj = j + dj
                # 인덱스 범위를 초과하지 않았을 때만
                if di >= 0 and dj >= 0 and di <= N-1 and dj <= N-1:
                    # 음수일 경우 - 붙여서 누적
                    if arr[di][dj] - arr[i][j] < 0:
                        sm += -(arr[di][dj] - arr[i][j])
                    else:
                        sm += arr[di][dj] - arr[i][j]
    print(f'#{test_case} {sm}')