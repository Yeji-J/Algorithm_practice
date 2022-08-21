import sys
sys.stdin = open("review_input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-1):
        # 조망권 확보
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            max_h = 0
            for j in range(i-2, i+3):       # 근처 빌딩의 최대 높이
                if j != i:
                    if arr[j] > max_h:
                        max_h = arr[j]
            ans += arr[i] - max_h


    print(f'#{test_case} {ans}')