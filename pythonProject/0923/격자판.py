import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def scan(n, i, j, st):
    if n == 7:              # 7자리 숫자완성
        if st not in ans:   # ans에 없으면 추가
            ans.append(st)
        return

    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):       # 동서남북
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:         # 범위 내일 때
            scan(n+1, ni, nj, st+arr[ni][nj])   # st에 해당 문자열 추가하고 넘기기


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    ans = []
    for i in range(4):
        for j in range(4):
            st = ''
            scan(0, i, j, st)

    print(f'#{tc} {len(ans)}')
