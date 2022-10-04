import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        S, B = b, a
    else:
        S, B = a, b

    # 최대 공약수
    cmn = 0
    for i in range(S, 0, -1):       # 더 작은수 ~ 1
        if S % i == 0 and B % i == 0:       # 두 수가 나누어 떨어지면
            cmn = i                         # 할당 & break
            break

    # 최소 공배수
    # 최대 공약수 * (a // 최대공약수) * (b // 최대공약수)
    ans = cmn * (a // cmn) * (b // cmn)
    print(ans)