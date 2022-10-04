import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

_ = int(input())
lst = list(map(int, input().split()))

# 올라가는 수열
stk_in = []
len_in = []

for x in lst:
    # 스택이 비었을 때
    if not stk_in:
        stk_in.append(x)
    else:
        # 스택의 마지막 수보다 작을 때
        if stk_in[-1] > x:
            len_in.append(len(stk_in))      # 지금까지 스택의 길이 저장
            stk_in = [x]    # 해당 값으로 스택 다시 시작

        # 스택의 마지막 수보다 같거나 클 때
        else:
            stk_in.append(x)

# 마지막 스택 길이 저장
len_in.append(len(stk_in))

# 내려가는 수열
stk_de = []
len_de = []

for num in lst:
    # 스택이 비었을 떄
    if not stk_de:
        stk_de.append(num)
    else:
        # 스택의 마지막 값보다 클 때
        if stk_de[-1] < num:
            len_de.append(len(stk_de))      # 지금까지 스택의 길이 저장
            stk_de = [num]          # 해당 값으로 스택 다시 시작

        # 스택의 마지막 수보다 작거나 같을 때
        else:
            stk_de.append(num)

# 마지막 스택 길이 저장
len_de.append(len(stk_de))

# 큰 값 찾기
if max(len_de) > max(len_in):
    ans = max(len_de)
else:
    ans = max(len_in)

print(ans)