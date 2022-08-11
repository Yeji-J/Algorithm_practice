import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
    cnts = 0
    for bit in range(1, 2 ** 12):
        sm = 0
        for i in range(12):
            if (bit >> i) & 1:
                print(bit, end=' ')
        print()