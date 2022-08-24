import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

heights = [int(input()) for _ in range(9)]
bit = [0] * 9
dwarfs = []                 # 일곱 난쟁이 키 리스트

for bit in range(2 ** 9):
    sm = 0                                  # 키 합

    for i in range(9):                      # 각 원소에 대해
        if (bit >> i) & 1:                  # 값이 존재하면 (비트 값이 1이면)
            sm += heights[i]                # 합에 누적
            dwarfs.append(heights[i])       # 난쟁이 리스트에 추가

    if sm == 100 and len(dwarfs) == 7:      # 합이 100이고 난쟁이가 7명이면
        dwarfs.sort()                       # 오름차순 출력
        for dwarf in dwarfs:
            print(dwarf)
        break
    else:
        dwarfs = []
