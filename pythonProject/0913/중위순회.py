import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def inord(n):       # 중위순회
    if n <= N:
        inord(n*2)      # 좌측노드 방문
        ans.append(arr[n])
        inord(n*2 + 1)      # 우측노드 방문

T = 10
for tc in range(1, T+1):
    N = int(input())
    root = 1
    arr = [0] * (N + 1)

    for i in range(1, N+1):
        lst = input().split()
        arr[i] = lst[1]

    ans = []
    inord(root)
    print("".join(ans))
