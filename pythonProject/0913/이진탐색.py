import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def inord(n):
    global cnt

    if n <= N:
        inord(n*2)
        # 트리 생성 (단위작업)
        lst[n] = cnt
        cnt += 1
        inord(n*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    root = 1
    # 이진트리 생성
    cnt = 1
    inord(root)
    print(f'#{tc} {lst[1]} {lst[N//2]}')

