import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def dfs(n):
    global ans

    # 종료조건
    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]
            # 해당 교환횟수(n)이고, 같은 lst 값이면 해 볼 필요 없음 (index 다르지만 중첩되는 경우)
            chk = int("".join(map(str, lst)))
            if(n, chk) not in v:
                dfs(n + 1)
                v.append((n, chk))

            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T+1):
    st, t = input().split()
    N = int(t)
    lst = []

    for ch in st:
        lst.append(int(ch))

    L = len(lst)
    v = []  # 해당 회수에 lst 값 처리했는지 체크

    ans = 0
    dfs(0)

    print(f'#{tc} {ans}')