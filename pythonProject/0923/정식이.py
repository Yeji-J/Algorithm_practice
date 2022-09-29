import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def hi():
    global ans

    for k in range(N2):
        for t in range(3):
            tmp2 = num2[:]
            if tmp2[k] != t:
                tmp2[k] = t

                # 10진수 변환
                res2 = 0
                for m in range(N2):
                    res2 += tmp2[N2 - m - 1] * (3 ** m)

                for n in lst1:
                    if n == res2:
                        ans = res2
                        return

T = int(input())
for tc in range(1, T+1):
    num1 = list(map(int, input()))
    num2 = list(map(int, input()))
    N1, N2 = len(num1), len(num2)

    # 2진수 -> 10진수 결과 리스트
    lst1 = []
    for i in range(N1):
        tmp = num1[:]

        # 0 -> 1, 1 -> 0
        if tmp[i] == 1:
            tmp[i] = 0
        else:
            tmp[i] = 1

        # 10진수 변환
        res = 0
        for j in range(N1):
            res += tmp[N1-j-1] * (2 ** j)
        lst1.append(res)

    ans = 0

    # 3진수 -> 10진수 함수 실행
    hi()
    print(f'#{tc} {ans}')


