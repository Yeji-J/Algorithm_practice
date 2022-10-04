import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def preord(n):
    if n:               # 자식 노드가 있으면
        ans.append(n)
        preord(ch1[n])
        preord(ch2[n])


T = int(input())
for tc in range(1, T+1):
    V = int(input())        # 정점 수
    lst = list(map(int, input().split()))
    root = 1                # root == 1번 정점
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(V-1):
        if ch1[lst[2*i]] == 0:
            ch1[lst[2*i]] = lst[2 * i + 1]
        else:
            ch2[lst[2*i]] = lst[2 * i + 1]

    print(ch1, ch2)
    ans = []
    preord(root)
    print(*ans)
