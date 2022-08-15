import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    idx = []
    for l in range(3):
        for r in range(3):
            idx.append((l, r))

    # 3 x 3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnts1 = [0] * 10
            for di, dj in idx:
                di = i + di
                dj = j + dj
                cnts1[sudoku[di][dj]] += 1
            for x in cnts1:
                if x >= 2:
                    ans = 0
                    break

    # 가로 세로
    for i in range(9):
        cnts2 = [0] * 10
        cnts3 = [0] * 10
        for j in range(9):
            cnts2[sudoku[i][j]] += 1
            cnts3[sudoku[j][i]] += 1
        for lst in cnts2, cnts3:
            for x in lst:
                if x >= 2:
                    ans = 0
                    break

    print(f'#{test_case} {ans}')



























    # for i in range(0, 9, 3):
    #     for j in range(0, 9, 3):
    #         for di, dj in idx:
    #             di = i + di
    #             dj = j + dj
    #             if cnts1[sudoku[di][dj]] <= 0:
    #                 ans = 0
    #                 break
    #             else:
    #                 cnts1[sudoku[di][dj]] -= 1
    #             print(cnts1)
    #             for k in range(9):
    #                 if cnts2[sudoku[k][dj]] <= 0:
    #                     ans = 0
    #                     break
    #                 else:
    #                     cnts2[sudoku[k][dj]] -= 1
    #                 if cnts3[sudoku[di][k]] <= 0:
    #                     ans = 0
    #                     break
    #                 else:
    #                     cnts3[sudoku[di][k]] -= 1
    #
    # print(cnts1, cnts2, cnts3)
    # print(f'#{test_case} {ans}')