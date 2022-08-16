import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(str, input())) for _ in range(5)]
    ans = ''
    # 단어 최대 길이
    len_max = 0
    for words in board:
        if len(words) > len_max:
            len_max = len(words)
    # index out of range 방지
    # 최대 길이보다 짧은 단어에 공백에는 ! 추가
    for words in board:
        if len(words) < len_max:
            for k in range(len_max - len(words)):
                words.append('!')
    # print(board)
    # '!'가 아니면 해당 문자 ans에 추가
    for j in range(len_max):
        letters = ''
        for i in range(5):
            if board[i][j] != '!':
                letters += board[i][j]
        ans += letters

    print(f'#{test_case} {ans}')