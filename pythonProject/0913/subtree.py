import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def counting(N):
    global cnts
    if N:       # 해당 노드 존재
        cnts += 1
        counting(ch1[N])
        counting(ch2[N])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(E):
        if ch1[arr[i*2]] == 0:
            ch1[arr[i*2]] = arr[i*2+1]
        else:
            ch2[arr[i*2]] = arr[i*2+1]
    cnts = 0
    counting(N)
    print(cnts)