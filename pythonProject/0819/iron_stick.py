import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    pars = list(str(input()))
    stk = []
    leng = []   # 막대 길이

    for i in range(len(pars)):
        if pars[i] == '(':
            stk.append([pars[i], i])    # 열린 괄호, 인덱스와 쌍으로 추가
        else:
            if stk:
                stk[-1][0] == '('
                leng.append([stk.pop()[1], i])  # 닫힌 괄호, 열린 괄호 인덱스와 쌍으로 추가

    # 레이저와 쇠막대 리스트 생성
    razar = []
    iron = []
    for a, b in leng:
        if b - a == 1:              # 차가 1이면 레이저
            razar.append([a, b])
        else:
            iron.append([a, b])

    # 막대 자르기
    cnts = len(iron)    # 막대 갯수 초깃값
    for r1, r2 in razar:
        for i1, i2 in iron:
            if i1 < r1 and r2 < i2:     # 레이저가 막대 범위 내에 존재
                cnts += 1               # cut

    print(f'#{test_case} {cnts}')