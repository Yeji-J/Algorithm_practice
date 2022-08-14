import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    area = []
    for _ in range(Q):
        area.append(list(map(int, input().split())))

    i = 1
    for x in area:
        for k in range(x[0]-1, x[1]):
            boxes[k] = i
        i += 1

    print(f'#{test_case}', *boxes)