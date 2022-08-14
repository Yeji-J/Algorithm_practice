import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(f'#{test_case} {ans}')

