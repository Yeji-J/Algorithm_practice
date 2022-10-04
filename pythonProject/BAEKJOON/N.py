import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
lst = list(map(int, input().split()))
std = min(lst)
cmn = 0

for i in range(std, 0, -1):
    cnts = 0
    for num in lst:
        if num % i == 0:
            cnts += 1
    if cnts == N:
        cmn = i
        break

if cmn == 1:
    print(1)
else:
    for j in range(1, cmn + 1):
        if cmn % j == 0:
            print(j)