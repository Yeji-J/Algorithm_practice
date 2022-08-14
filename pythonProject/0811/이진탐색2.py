import sys
sys.stdin = open("../input.txt", "r")

def binarySearch(arr, N, D):
    s = 0
    e = N - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] == D:
            return m + 1 # 인덱스 0부터
        elif arr[m] < D:
            s = m + 1 # start point = m 보다 하나 큰 인덱스
        else:
            e = m - 1 # end point = m보다 하나 작은 인덱스
    return 0


T = int(input())
for test_case in range(1, T+1):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = binarySearch(arr, N, D)
    print(f'#{test_case} {ans}')



