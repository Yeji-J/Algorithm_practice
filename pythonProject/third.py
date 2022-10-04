import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')


def asd(a):
    if a <= N:
        asd(a*2)
        print(al_lst[a], end="")
        asd(a*2 + 1)


for T in range(1, 11):
    N = int(input())        # 정점의 총 수
    al_lst = [0] * (N + 1)
    for i in range(N):
        lst = input().split()
        al_lst[i+1] = lst[1]

    print(f'#{T}', end=" ")
    asd(1)
    print()

