import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# POST 순회 (root 기준)
def post(n):
    if node[n]:          # lst[n]자리에 노드가 존재
        # 연산자일 때
        if node[n] == '*':
            return post(ch1[n]) * post(ch2[n])
        elif node[n] == '+':
            return post(ch1[n]) + post(ch2[n])
        elif node[n] == '-':
            return post(ch1[n]) - post(ch2[n])
        elif node[n] == '/':
            return post(ch1[n]) / post(ch2[n])

        # 연산자가 아니라면 숫자 리턴
        else:
            return int(node[n])



T = 10
for tc in range(1, T + 1):

    N = int(input())        # 노드 수

    node = [0] * (N + 1)    # 노드 리스트

    ch1 = [0] * (N + 1)     # left child
    ch2 = [0] * (N + 1)     # right child

    # 트리 구조에 맞게 저장
    for _ in range(N):
        lst = input().split()
        p = int(lst[0])
        node[p] = lst[1]
        if len(lst) == 4:
            ch1[p], ch2[p] = int(lst[2]), int(lst[3])

    ans = post(1)       # root == 1

    print(f'#{tc} {int(ans)}')
