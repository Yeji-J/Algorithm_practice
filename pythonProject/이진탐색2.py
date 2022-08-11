import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    i = 0

    for i in range(0, 10, 2):
        max_i = i
        min_i = i
        for j in range(i, N):

            if lst[j] > lst[max_i]:
                max_i = j
            if lst[j] < lst[min_i]:
                min_i = j
        print(lst[max_i], lst[min_i])

    print(f'#{test_case} {lst}')