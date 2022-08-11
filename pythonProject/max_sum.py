import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 3):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    diagonal1 = diagonal2 = 0
    col_max = row_max = 0
    ans = 0

    for i in range(100):
        diagonal1 += arr[i][i]
        diagonal2 += arr[99-i][i]

        if diagonal1 > diagonal2:
            ans = diagonal1
        else:
            ans = diagonal2

        col_sum = row_sum = 0
        for j in range(100):
            col_sum += arr[i][j]
            if col_sum > col_max:
                col_max = col_sum

            row_sum += arr[j][i]
            if row_sum > row_max:
                row_max = row_sum

        if row_max > ans:
            ans = row_max
        if col_max > ans:
            ans = col_max


    print(f'#{test_case} {ans}')


