import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')


T = int(input())
for test_case in range(1, T + 1):
    card = input()

    S = []
    D = []
    H = []
    C = []

    for i in range(0, len(card)-2, 3):
        if card[i] == 'S':
            if card[i+1] != 0:
                S.append(int(card[i+1][i+2]))
            else:
                S.append(int(card[i+2]))

        elif card[i] == 'D':
            if card[i+1] != 0:
                D.append(int(card[i+1][i+2]))
            else:
                D.append(int(card[i+2]))
        elif card[i] == 'H':
            if card[i+1] != 0:
                H.append(int(card[i+1][i+2]))
            else:
                H.append(int(card[i+2]))
        elif card[i] == 'C':
            if card[i+1] != 0:
                C.append(int(card[i+1][i+2]))
            else:
                C.append(int(card[i+2]))



    print(H, D, C, S)