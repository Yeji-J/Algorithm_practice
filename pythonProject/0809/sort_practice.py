import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i+1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(f'#{test_case}', *arr)