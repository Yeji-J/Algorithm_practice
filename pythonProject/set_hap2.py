import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ans = 0
    for bit in range(2 ** 12):
        sm = 0
        cnts = 0
        for i in range(12):
            if (bit >> i) & 1:
                sm += A[i]
                cnts += 1
        if sm == K and cnts == N:
            ans += 1

    print(f'#{test_case} {ans}')