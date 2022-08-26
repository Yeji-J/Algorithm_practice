import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')


N = int(input())
switch = list(map(int, input().split()))
ppl = []

for _ in range(int(input())):
    ppl.append(list(map(int, input().split())))

for one in ppl:
    # 남학생일 때
    if one[0] == 1:
        for i in range(N):
            if (i+1) % one[1] == 0:             # 스위치 번호(인덱스 + 1)가 배수면
                if switch[i] == 0:              # 스위치의 ON / OFF
                    switch[i] = 1
                else:
                    switch[i] = 0

    # 여학생일 때
    else:
        k = 1
        left, right = 0, 0
        while left == right:             # 양 옆 스위치가 같을 때
            left, right = switch[one[1] - k], switch[one[1] + k]
            if 0 <= one[1] - k < N and 0 <= one[1] + k < N:
                if switch[left] == 0:       # ON / OFF
                    left, right = 1, 1
                else:                       # ON / OFF
                    left, right = 0, 0
                k += 1

print(switch)

