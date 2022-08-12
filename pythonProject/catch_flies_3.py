import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(5)]
    max_cross = 0
    max_x = 0
    for i in range(N):
        for j in range(N):
            cross_sum = 0
            for n in range(2*M):
                if i + n <= 99 and i - n >= 0 and j + n <= 99 and j - n >= 0:
                    cross_sum += (area[i][j-n] + area[i-n][j])
            cross_sum -= area[i][j]

            if max_cross < cross_sum:
                max_cross = cross_sum

            x_sum = 0
            for k in range(M):
                if k != 0 and i + k <= N-1 and i - k >= 0 and j + k <= N-1 and j - k >= 0:
                    x_sum += (area[i-k][j-k] + area[i+k][j-k] + area[i-k][j+k] + area[i+k][j+k])
            x_sum += area[i][j]

            if max_x < x_sum:
                max_x = x_sum

    print(max_x, max_cross)