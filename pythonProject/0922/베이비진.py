import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def check():
    global ans, r1, r2

    for k in range(10):
        if p1[k] >= 3:
            r1 += 1

            if r1 > r2:
                ans = 1
                return

        if p2[k] >= 3:
            r2 += 1

            if r2 > r1:
                ans = 2
                return

    for j in range(8):
        if p1[j] >= 1 and p1[j+1] >= 1 and p1[j+2] >= 1:
            r1 += 1

            if r1 > r2:
                ans = 1
                return

        if p2[j] >= 1 and p2[j+1] >= 1 and p2[j+2] >= 1:
            r2 += 1

            if r2 > r1:
                ans = 2
                return

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    p1 = [0] * 10
    p2 = [0] * 10

    ans = 0

    r1, r2 = 0, 0
    for i in range(0, 11, 2):
        p1[card[i]] += 1
        if i >= 4:
            check()
            if ans:
                break

        p2[card[i+1]] += 1

        if i >= 4:
            check()
            if ans:
                break

    print(f'#{tc} {ans}')