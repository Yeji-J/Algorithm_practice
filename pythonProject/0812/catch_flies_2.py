import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    # 파리채 영역
    swat = []
    for k in range(M):
        for l in range(M):
            swat.append((k, l))
    # 파리 잡기
    fly_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sm = 0
            for di, dj in swat:
                sm += area[i + di][j + dj]
            if fly_max < sm:
                fly_max = sm
    print(f'#{test_case} {fly_max}')

