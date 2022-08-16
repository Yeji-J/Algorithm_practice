import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    words = [list(map(str, input())) for _ in range(N)]
    ans = []
    # 가로
    for i in range(N):
        lst1 = []
        for j in range(N - M + 1):
            word1 = ''
            for k in range(j, j + M):
                if k < N:
                    word1 += words[i][k]
                    k += 1
            if word1[:] == word1[::-1]:
                ans.append(word1)

    # 세로
    for i in range(N - M + 1):
        lst2 = []
        for j in range(N):
            word2 = ''
            for k in range(i, i + M):
                if k < N:
                    word2 += words[k][j]
                    k += 1
            if word2[:] == word2[::-1]:
                ans.append(word2)

    print(f'#{test_case}', *ans)


