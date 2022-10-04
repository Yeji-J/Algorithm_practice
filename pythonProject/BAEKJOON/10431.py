import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    std = list(map(int, input().split()))
    std.pop(0)  # tc 번호 빼고
    cnts = 0

    for i in range(20):
        for j in range(i, 20):
            if std[i] > std[j]:     # 앞 사람이 더 크다면
                std[i], std[j] = std[j], std[i]     # 자리 바꾸고
                cnts += 1           # + 1

    print(f'{tc} {cnts}')