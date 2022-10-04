import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def preorder(n):
    if n:
        print(n, end=' ')        # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    V = int(input())            # 노드 수
    arr = list(map(int, input().split()))
    root = 1

    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(V-1):
        # p 부모 c 자식 노드
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    print(f'#{tc}', end=' ')
    preorder(root)