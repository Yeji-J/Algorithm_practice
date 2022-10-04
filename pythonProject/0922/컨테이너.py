import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def nCr(n, r, s):       # n개 중에서 r개 고르고 s(idx)부터 시작
    global cMax

    # r개 다 고르면 종료
    if r == 0:
        lst.sort(reverse=True)
        k = 0

        # 트럭에 맞게 컨테이너 싣기
        for i in range(M):
            if lst[i] <= MW[k]:
                ans[k] = lst[i]
                k += 1

        # 최댓값 비교
        if sum(ans) > cMax:
            cMax = sum(ans)
        return

    else:
        for i in range(s, n-r+1):
            lst[r-1] = NW[i]
            nCr(n, r-1, i+1)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N : 컨테이너 수 M : 트럭 수
    NW = list(map(int, input().split()))    # 컨테이너 용량
    MW = list(map(int, input().split()))    # 트럭 용량

    # 트럭 용량 정렬
    MW.sort(reverse=True)

    if N < M:
        M = N

    cMax = 0
    ans = [0] * M
    lst = [0] * M
    nCr(N, M, 0)

    print(f'#{tc} {cMax}')