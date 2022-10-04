import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')


def counting():
    global ans
    for k in range(0, len(st)-2, 3):
        card.append([st[k], st[k + 1], st[k + 2]])

    for lst in card:
        if lst in finished:
            ans = ['ERROR']
            return ans
        else:
            if lst[1] != '0':
                num = int(lst[1] + lst[2])
            else:
                num = int(lst[2])

            if lst[0] == 'S':
                S.append(num)
            elif lst[0] == 'D':
                D.append(num)
            elif lst[0] == 'H':
                H.append(num)
            else:
                C.append(num)

            finished.append(lst)

    for arr in [S, D, H, C]:
        ans.append(13 - len(arr))

    return ans


T = int(input())
for test_case in range(1, T + 1):
    st = list(map(str, input()))

    S = []
    D = []
    H = []
    C = []

    card = []
    finished = []
    ans = []

    counting()

    print(f'#{test_case}', *ans)