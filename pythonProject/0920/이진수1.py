import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

dct = {
    'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

T = int(input())
for tc in range(1, T + 1):
    _, st = input().split()

    ans = ''
    for ch in st:
        if ch.isdigit():        # 숫자일 때

            # 하나의 16진수는 4개의 2진수를 표시 : 따라서 범위 4
            for i in range(3, -1, -1):

                # 비트 값이 있으면 1, 없으면 0 추가
                ans += '1' if (int(ch) & (1 << i)) else '0'

        else:               # 문자일 때
            ans += dct[ch]

    print(f'#{tc} {ans}')


