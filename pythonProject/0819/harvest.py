import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    food = [list(map(int,input())) for _ in range(N)]
    sm = 0
    k = (N - 1) // 2        # k 시작점 == N 중간 값
    for i in range(N):
        for j in range(k, N-k):     # j: K ~ N-K-1
            sm += food[i][j]        # 농작물 더하기
        if i < (N-1)//2:        # 가운데행 이전이면 k - 1
            k -= 1
        elif i >= (N-1)//2:     # 가운데행 포함 이후면 k + 1
            k += 1

    print(f'#{test_case} {sm}')