import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input()))
    n = 0
    ans = []
    for i in range(len(lst)):
        n = lst[i] + n*2        # 2진수니까
        if i % 7 == 6:          # 7 bit씩
            ans.append(n)
            n = 0

    print(f'#{tc}', *ans)