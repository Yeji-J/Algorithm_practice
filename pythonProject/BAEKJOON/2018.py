import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
cnts = 0
for i in range(1, N+1):         # N : 1 -> N-1
    sm = 0
    k = i
    while True:
        sm += k
        k += 1
        if sm > N:
            break
        if sm == N:
            cnts += 1

print(cnts)
