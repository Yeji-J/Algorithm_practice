import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def R(x, M):
    cnts = 0
    for _ in range(N):  # N번 이동
        while x < M and cnts < N:  # 처음 : max 직전까지 +1
            x += 1
            cnts += 1
            if cnts == N:
                return x

        if x == M:  # max 닿았을 때
            while x > 0 and cnts < N:  # 0 직전까지 -1
                x -= 1
                cnts += 1
                if cnts == N:
                    return x

        if x == 0:  # 0 닿았을 때
            while x < M and cnts < N:  # max 직전까지 +1
                x += 1
                cnts += 1
                if cnts == N:
                    return x

W, H = map(int, input().split())
p, q = map(int, input().split())
N = int(input())

print(R(p, W), R(q, H))