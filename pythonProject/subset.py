import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def f(i, N):
    global cnts
    if i == N:              # 모든 원소를 다 돌았을 때
        s = 0
        for i in range(N):
            if bit[i]:      # 값이 있다면 더하기
                s += arr[i]
        if s == K:          # K와 합이 같다면
            cnts += 1       # cnts +1
    else:
        for k in [0, 1]:
            bit[i] = k      # i가 들어갈 때 & 안 들어갈 때
            f(i+1, N)       # 다음 i로 넘어가기

    return cnts


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = [0] * N
    cnts = 0

    print(f'#{test_case} {f(0, N)}')