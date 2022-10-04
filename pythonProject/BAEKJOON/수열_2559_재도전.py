import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N, D = map(int, input().split())
lst = list(map(int, input().split()))

sm = sum(lst[0:D])
tmp = sm
for i in range(N-D):
    tmp = (tmp - lst[i] + lst[i+D])
    if sm < tmp:
        sm = tmp


print(sm)