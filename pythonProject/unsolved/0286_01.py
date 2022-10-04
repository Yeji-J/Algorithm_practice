import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        lst1, lst2 = A, B            # lst1 : 더 짧은 쪽 lst2 :  더 긴 쪽
        len1, len2 = N, M
    else:
        lst1, lst2 = B, A
        len1, len2 = M, N

    ans = 0
    for i in range(len2 - len1 + 1):
        total = 0
        tmp = lst2[i:i+len1]
        for j in range(len1):
            total += tmp[j] * lst1[j]

        if ans < total:
            ans = total

    print(f'#{test_case} {ans}')


