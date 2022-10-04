import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

move_dic = {'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1),
            'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}
chr_dic = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8'}
num_dic = {v:k for k, v in chr_dic.items()}

K, S, N = input().split()
move = [input() for _ in range(int(N))]

Ki, Kj = (int(chr_dic[K[0]]), int(K[1]))            # King의 위치
Si, Sj = (int(chr_dic[S[0]]), int(S[1]))            # Stone의 위치

for m in range(int(N)):

    mi, mj = (int(move_dic[move[m]][0]), int(move_dic[move[m]][1]))     # 이동 좌표
    Kim, Kjm = Ki + mi, Kj + mj       # King 이동할 위치
    Sim, Sjm = Si + mi, Sj + mj       # Stone 이동할 위치

    if 1 <= Kim <= 8 and 1 <= Kjm <= 8:         # King 이동 가능한 범위 내
        if Kim == Si and Kjm == Sj:  # King 이동하려는 곳에 돌이 있으면
            if 1 <= Sim <= 8 and 1 <= Sjm <= 8:  # Stone 이동 가능한 범위 내
                Ki, Kj = (int(chr_dic[num_dic[str(Kim)]]), Kjm)
                Si, Sj = (int(chr_dic[num_dic[str(Sim)]]), Sjm)

        else:           # King 이동하려는 곳에 돌이 없으면
            Ki, Kj = (int(chr_dic[num_dic[str(Kim)]]), Kjm)

print(num_dic[str(Ki)]+str(Kj))
print(num_dic[str(Si)] + str(Sj))









