import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def cmn():
    lst = num_lst
    cnts = 0
    while lst:
        num = lst[0]
        for j in range(len(lst)):
            if lst[j] % num == 0:
                cnts += 1
                if cnts == K:
                    return lst[j]
                else:
                    lst[j] = 0
        tmp = []
        for k in lst:
            if k != 0:
                tmp += [k]
        lst = tmp

N, K = map(int, input().split())
num_lst = []

# 2부터 N까지의 정수
for i in range(2, N+1):
    num_lst += [i]

print(cmn())





