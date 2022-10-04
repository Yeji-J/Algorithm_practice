import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # N: 점원 수 B: 탑의 높이
    H = list(map(int, input().split()))

    res = []
    for i in range(1, 2 ** N):
        lst = []
        for j in range(N):
            if 1 & (i >> j):
                lst.append(H[j])
        if sum(lst) >= B:
            res.append(sum(lst))

    ans = min(res) - B

    print(f'#{tc} {ans}')


