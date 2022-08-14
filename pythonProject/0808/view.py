import sys
sys.stdin = open("input.txt", "r")

for t in range(3):
    T = int(input())
    box = list(map(int, input().split()))
    counts = 0
    for i in range(2, T - 1):
        if box[i-2] < box[i] and box[i-1] < box[i] and box[i+1] < box[i] and box[i+2] < box[i]:
            bldg_max = 0
            for j in range(i-2, i+3):
                if j != i and box[j] > bldg_max:
                    bldg_max = box[j]
            counts += (box[i]-bldg_max)

    print(f'#{t+1} {counts}')