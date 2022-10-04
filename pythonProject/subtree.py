import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def ord(N):
    global cnts
    if N:
        cnts += 1
        ord(ch1[N])
        ord(ch2[N])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    for i in range(E):
        if ch1[arr[2 * i]] == 0:
            ch1[arr[2 * i]] = arr[2 * i + 1]
        else:
            ch2[arr[2 * i]] = arr[2 * i + 1]

    cnts = 0
    ord(N)
    print(f'#{tc} {cnts}')