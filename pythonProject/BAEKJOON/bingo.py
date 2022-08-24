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
    for lst1 in bingo:
        if sum(lst1) == 0:      # 행의 합이 0일 때(빙고)
            return 1
    return 0            # 모든 행을 돌아도 빙고가 없다면

# 열 빙고 확인
def columns():
    col = list(zip(*bingo))     # 열의 합이 0일 때(빙고)
    for lst2 in col:
        if sum(lst2) == 0:
            return 1
    return 0            # 모든 열을 돌아도 빙고가 없다면

bingo = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

turns = 0
while turns <= 25:      # 25개 숫자 불릴 때까지만

    cnts = 0    # 빙고 갯수 카운트
    zero = 0    # 체크된 숫자 카운트

    mcNum = mc.pop(0)       # 사회자 숫자 리스트에서 꺼내기
    turns += 1              # 숫자 부르는 횟수

    for i in range(5):
        for j in range(5):
            if bingo[i][j] == mcNum:    # 사회자가 부른 숫자와 같으면
                bingo[i][j] = 0             # 0으로 초기화

    for lst in bingo:
        for num in lst:
            if num == 0:
                zero += 1

    # 불린 숫자가 12(빙고가 가능한 최소 숫자 갯수)보다 클 때
    if zero >= 12:
        cnts += (cross1() + cross2() + rows() + columns())

    if cnts >= 3:               # 빙고 갯수가 3보다 크면
        print(25-len(mc))       # mc 전체 숫자 - 남아있는 숫자
        break               # while 종료
