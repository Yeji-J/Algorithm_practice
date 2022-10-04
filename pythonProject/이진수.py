import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    num = input()
    ans = []
    for i in range(0, len(num), 7):
        res = 0
        for j, tmp in enumerate(num[i:i+7]):    # 7bit씩 묶기
            if tmp == '1':
                res += 2 ** (6-j)
        ans.append(res)

    print(f'#{tc}', *ans)
