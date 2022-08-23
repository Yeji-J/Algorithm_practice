import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def postFix(cal_in):
    stk = []
    cal_dict = {'*': 2, '+': 1}  # 연산자 우선순위

    for x in cal_in:                                        # 입력 받은 수식의 각 요소에 대해
        if x == '*' or x == '+':                            # 연산자라면
            while stk and cal_dict[stk[-1]] >= cal_dict[x]:  # 스택이 not empty && top이 연산자의 value보다 크다면
                res.append(stk.pop())                   # pop해서 nums에 추가
            stk.append(x)                               # 해당 연산자 스택에 추가
        else:
            res.append(x)                               # 숫자라면 nums에 추가

    if stk:                         # 스택에 요소가 있다면
        for i in range(len(stk)):   # 모든 요소 pop해서 nums에 추가
            res.append(stk.pop())

    return res

T = 10
for test_case in range(1, T+1):
    _ = input()
    cal_in = input()
    res = []
    postFix(cal_in)

    stk2 = []
    for x in res:
        if x == '+':                                         # 더하기 연산자
                cal_num = int(stk2.pop()) + int(stk2.pop())     # pop한 값 두 개 더하기
                stk2.append(cal_num)
        elif x == '*':                                      # 곱하기 연산자
            cal_num = int(stk2.pop()) * int(stk2.pop())     # pop한 값 두 개 곱하기
            stk2.append(cal_num)

        else:                                               # 숫자면 그냥 추가
            stk2.append(x)

    print(f'#{test_case}', stk2.pop())

