import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

A =[1, 2, 3, 4, 5,]
res = []
for bit in range(2 ** 5):
    sm = 0
    cnt = 0
    lst = []
    for i in range(5):
        if (bit >> i) & 1:
            sm += A[i]
            lst += [A[i]]
            cnt += 1
    if sm == 10:
        res.append(lst)

print(res)