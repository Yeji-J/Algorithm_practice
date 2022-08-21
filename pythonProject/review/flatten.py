import sys
sys.stdin = open("review_input.txt", "r")

def sortArr(arr):
    for m in range(len(arr)):
        for n in range(m + 1, len(arr)):
            if arr[m] > arr[n]:
                arr[m], arr[n] = arr[n], arr[m]

T = 10
for test_case in range(1, T + 1):
    D = int(input())
    arr = list(map(int, input().split()))

    i = 0
    while i < D:
        sortArr(arr)

        arr[-1] -= 1
        arr[0] += 1

        if arr[-1] - arr[0] <= 1:
            break

        i += 1

    sortArr(arr)    # 최종 dump 이후 최대 최솟값

    print(f'#{test_case} {arr[-1] - arr[0]}')
