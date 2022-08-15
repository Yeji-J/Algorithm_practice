import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    res = []

    for i in range(N):
        cnts1 = cnts2 = 0
        for j in range(N):
            # 가로줄 탐색
            if puzzle[i][j] == 1: # 값이 1일 때 하나씩 누적
                cnts1 += 1
            if puzzle[i][j] == 0: # 0을 만나면 기존 누적 값 저장 후 0으로 초기화
                if cnts1 != 0:
                    res.append(cnts1)
                    cnts1 = 0
            # 세로줄 탐색
            if puzzle[j][i] == 1:
                cnts2 += 1
            if puzzle[j][i] == 0:
                if cnts2 != 0:
                    res.append(cnts2)
                    cnts2 = 0
        # 줄이 바뀔 때 해당 값이 0이 아니면 추가
        if cnts1 != 0:
            res.append(cnts1)
        if cnts2 != 0:
            res.append(cnts2)

    ans = 0
    for k in res:
        if k == K: # 단어가 들어갈 수 있는 곳이면 + 1
            ans += 1

    print(f'#{test_case} {ans}')