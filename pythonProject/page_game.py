import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    cnts_A = 0
    cnts_B = 0

    As = 1
    Ae = P
    while True:
        Ac = int((As + Ae) // 2)
        if Ac < A:
            As = Ac
            cnts_A += 1
        if Ac > A:
            Ae = Ac
            cnts_A += 1
        if Ac == A:
            break
    Bs = 1
    Be = P

    while True:
        Bc = int((Bs + Be) // 2)
        if Bc < B:
            Bs = Bc
            cnts_B += 1
        if Bc > B:
            Be = Bc
            cnts_B += 1
        if Bc == B:
            break

    if cnts_B > cnts_A:
        ans = 'A'
    elif cnts_B < cnts_A:
        ans = 'B'
    else:
        ans = 0

    print(f'#{test_case} {ans}')