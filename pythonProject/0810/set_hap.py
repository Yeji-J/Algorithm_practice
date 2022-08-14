import sys
sys.stdin = open("../input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):
#     arr = list(map(int, input().split()))
#     print(arr)
#     n = len(arr)
#
#     for i in range(2**n): # 2^n개의 부분집합
#         for j in range(n):
#             if i & j(n):
#                 print(arr[j], end=', ')
#             print()
#         print()


T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    ans = 0
    N = len(lst)  # N bit (lst member: N)

    for bit in range(1, 2 ** N):  # 2**N개의 부분집합
        sm = 0
        for i in range(0, N):  # 모든 리스트 인덱스에 대해
            if (bit >> i) & 1: # 비트 값이 1일 경우
                sm += lst[i]

        if sm == 0:  # 합이 0일 때
            ans = 1
            break
    print(f'#{test_case} {ans}')

