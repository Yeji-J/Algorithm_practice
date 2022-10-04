import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
cnts = 0
num = N

while True:
    cnts += 1
    tmp = 0
    for x in str(num):
        tmp += int(x)

    num = str(num)[-1] + str(tmp)[-1]

    if int(num) == N:
        break

print(cnts)