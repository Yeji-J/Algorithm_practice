import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]

    # 종료시간 기준으로 정렬
    lst.sort(key=lambda x:x[1])

    ans = 1
    s, e = lst[0][0], lst[0][1]

    for i in range(1, len(lst)):
        ns, ne = lst[i][0], lst[i][1]
        if e <= ns:
            ans += 1
            e = ne

    print(f'#{tc} {ans}')
