import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    cal_in = input()
    stk = []
    nums = []
    cal_dict = {'*' : 2, '+' : 1}               # 연산자 우선순위

    for x in cal_in:                # 입력 받은 수식의 각 요소에 대해
        if x == '*' or x == '+':                                # 연산자라면
            while stk and cal_dict[stk[-1]] >= cal_dict[x]:     # 스택이 비어있지 않고 && top이 연산자의 value보다 크다면
                nums.append(stk.pop())                          # pop해서 nums에 추가
            stk.append(x)                               # 해당 연산자 스택에 추가
        else:
            nums.append(x)          # 숫자라면 nums에 추가

    if stk:                         # 스택에 요소가 있다면
        for i in range(len(stk)):   # 모든 요소 pop해서 nums에 추가
            nums.append(stk.pop())

    print(f'#{test_case}', "".join(nums))


