import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) // 10
    lst = [0] * (N+1)

    lst[1], lst[2] = 1, 3   # 초깃값 : N==10 & N == 20
    for i in range(3, N+1): # N == 30 부터
        lst[i] = lst[i-1] + lst[i-2] * 2

    print(f'#{test_case} {lst[N]}')