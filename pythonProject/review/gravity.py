import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    _ = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(len(arr)):   # 각 박스 더미에 대해
        cnts = 0
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:      # 다음에 오는 더미보다 크다면
                cnts += 1            # 낙차 + 1

        if ans < cnts:
            ans = cnts

    print(f'#{test_case} {ans}')




