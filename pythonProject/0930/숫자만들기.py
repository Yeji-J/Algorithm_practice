import sys
sys.stdin = open("input.txt", "r")

def comb():

    if sum(used) == (N-1)(N-2)//2:
        if used not in lst:
            lst.append(used)
        return

    for i in range(N-1):
        if not used[i]:
            used[i] = i
            comb()
            used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_num = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    lst = []
    used = [0] * (N-1)  # 사용된 리스트

    comb()

    print(lst)





