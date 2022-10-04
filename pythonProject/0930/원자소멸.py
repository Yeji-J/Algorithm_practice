import sys
sys.stdin = open("input.txt", "r")

D = {   # 상 하 좌 우
    0:(-1,0), 1:(1,0), 2:(0,-1), 3:(0,1)
}

def simul():
    global total
    sec = 0
    while sec <= 2000:
        print(dot)
        for one in dot:
            di, dj = D[one[2]]          # 이동방향에 따라
            one[0], one[1] = one[0]+di, one[1]+dj          # 계속 이동
        print(dot)
        # 1초 이동 후 비교
        for i in range(N):
            for j in range(i, N):
                # 아직 살아있는 원자만
                if power[i] and power[j]:
                    # x, y 좌표가 같을 때
                    if dot[i][0] == dot[j][0] and dot[i][1] == dot[j][1]:
                        total += (power[i] + power[j])
                        power[i], power[j], dot[i][-1], dot[j][-1] = 0, 0, -1, -1

                    # x 좌표 1차이, 방향이 좌우일 때
                    if abs(dot[i][0]-dot[j][0]) == 1 and D[dot[i][-1]][1] + D[dot[j][-1]][1] == 0:
                        # 더 작은 쪽 : 우, 더 큰 쪽 : 좌
                        if dot[i][0] < dot[j][0]:
                            if dot[i][-1] == 3 and dot[j][-1] == 2:
                                total += (power[i] + power[j])
                                power[i], power[j], dot[i][-1], dot[j][-1] = 0, 0, -1, -1
                        else:
                            if dot[j][-1] == 3 and dot[i][-1] == 2:
                                total += (power[i] + power[j])
                                power[i], power[j], dot[i][-1], dot[j][-1] = 0, 0, -1, -1

                    # y 좌표 1차이, 방향이 상하일 때
                    if abs(dot[i][1]-dot[j][1]) == 1 and D[dot[i][-1]][0] + D[dot[j][-1]][0] == 0:
                        # 더 작은 쪽 : 상, 더 큰 쪽 : 하
                        if dot[i][1] < dot[j][1]:
                            if dot[i][-1] == 0 and dot[j][-1] == 1:
                                total += (power[i] + power[j])
                                power[i], power[j], dot[i][-1], dot[j][-1] = 0, 0, -1, -1
                        else:
                            if dot[j][-1] == 0 and dot[i][-1] == 1:
                                total += (power[i] + power[j])
                                power[i], power[j], dot[i][-1], dot[j][-1] = 0, 0, -1, -1
                    print(power)
                    if sum(power) == 0:
                        return
        sec += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dot = []
    power = []
    for _ in range(N):
        x, y, d, p = map(int, input().split())
        dot.append([x,y,d])
        power.append(p)
    print(power)

    total = 0
    simul()
    print(total)

















                    # # power 0인 애들 제거
                    # for _ in power:
                    #     p = power.pop(0)
                    #     if p != 0:
                    #         power.append(p)
                    #
                    # # 충돌된 원자 제거
                    # for _ in dot:
                    #     o = dot.pop(0)
                    #     if o[-1] != -1:
                    #         dot.append(o)

