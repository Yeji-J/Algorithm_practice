import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def bs(s, e, key):
    d = 0           # 오 1, 왼 -1
    while s <= e:  # 키 값을 찾을 때까지

        m = (s + e) // 2

        if key == A[m]:
            return 1

        elif key < A[m]:
            if d == -1:
                return 0

            d = -1
            e = m - 1

        else:
            if d == 1:
                return 0

            d = 1
            s = m + 1

    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : len(A)  M : len(B)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnts = 0

    for key in B:
        cnts += bs(0, len(A)-1, key)

    print(f'#{tc} {cnts}')
