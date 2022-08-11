import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    mx = 0 # 초깃값 : 양수
    mn = 100000 # 초깃값 : 가장 큰 수
    for num in list:
        if mn > num:
            mn = num
        elif mx < num:
            mx = num