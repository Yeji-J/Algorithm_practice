import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')


# 후위순회 LRV
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())     # N 노드 개수 M 리프 노드 개수 L 값 출력

    lst = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        lst[a] = b


