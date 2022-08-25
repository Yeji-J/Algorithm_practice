import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# 우하향 대각선 빙고 확인
def cross1():
    for i in range(5):
        if bingo[i][i] != 0:
            return 0
    return 1

# 우상향 대각선 빙고 확인
def cross2():
    for i in range(5):
        if bingo[i][4-i] != 0:
            return 0
    return 1

# 행 빙고 확인
def rows():
    sm = 0                  # 모든 행을 돌았을 때 빙고 개수
    for lst1 in bingo:
        if sum(lst1) == 0:
            sm += 1
    return sm

# 열 빙고 확인
def columns():              # 모든 열을 돌았을 때 빙고 개수
    sm = 0
    col = list(zip(*bingo))
    for lst2 in col:
        if sum(lst2) == 0:
            sm += 1
    return sm

bingo = [list(map(int, input().split())) for _ in range(5)]
mc = []
# 사회자 숫자
for _ in range(5):
    mc += list(map(int, input().split()))

for turns in range(1, 26):      # 25개 숫자 불릴 때까지만
    cnts = 0    # 빙고 개수 카운트

    mcNum = mc.pop(0)       # 사회자 숫자 리스트에서 꺼내기

    for i in range(5):
        for j in range(5):
            if bingo[i][j] == mcNum:    # 사회자가 부른 숫자와 같으면
                bingo[i][j] = 0             # 0으로 초기화

    # 불린 숫자가 12(빙고가 가능한 최소 숫자 개수)보다 클 때
    if turns >= 12:
        cnts = cross1() + cross2() + rows() + columns()

    if cnts >= 3:               # 빙고 개수가 3보다 크면
        print(turns)       # mc 전체 숫자 - 남아있는 숫자
        break               # while 종료
