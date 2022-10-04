import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())

for tc in range(1, T + 1):
    # N : 노드수 M : 리프노드 개수 L: 값을 출력할 노드번호
    N, M, L = map(int, input().split())
    lst = [0] * (N + 1)

    for _ in range(M):
        n, v = map(int, input().split())
        lst[n] = v

    for i in range(N, 1, -1):
        lst[i//2] += lst[i]

    print(f'#{tc} {lst[L]}')