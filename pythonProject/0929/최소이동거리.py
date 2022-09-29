import sys
sys.stdin = open("input.txt", "r")

def go(si, total):
    global ans

    if total >= ans:
        return

    # 마지막 노드에 도달하면 종료
    if si == N:
        ans = min(ans, total)
        return

    for ni in range(len(arr[si])):
        if arr[si][ni] != 0:
            go(ni, total + arr[si][ni])


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())        # N:마지막 연결지점 번호
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w       # 일방향

    ans = 10 * E
    go(0, 0)       # 0번부터 이동
    print(f'#{tc} {ans}')

