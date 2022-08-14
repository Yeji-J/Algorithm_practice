import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(0, 10, 2):
        min_i = max_i = i
        for j in range(i, N):
            if lst[min_i] > lst[j]:
                min_i = j
            if lst[max_i] < lst[j]:
                max_i = j
        lst[max_i], lst[i] = lst[i], lst[max_i]
        if min_i == i:
            min_i = max_i
        lst[min_i], lst[i+1] = lst[i+1], lst[min_i]

    print(f'#{test_case}', *lst[:10])

