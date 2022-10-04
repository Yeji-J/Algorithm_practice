import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())     # N: 사람 M: 초 K: 개수
    ppl = list(map(int, input().split()))
    ppl.sort(reverse=True)

    fish = 0
    ans = ''

    if M <= ppl[0]:
        fish += K
        fish -= 1
        while True:
            rest = ppl[0] - M
            ppl.pop(0)
            if ppl:
                if rest + ppl[0] >= M:
                    fish += K
                    fish -= 1
                else:
                    if fish >= 1:
                        fish -= 1
                    else:
                        ans = 'impossible'
            else:
                ans = 'possible'
                break
    else:
        ans = 'impossible'

    print(ans)