from itertools import combinations

data = input()

stack = []
array = []
ans = []

# 인덱스와 함께 저장
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        num = stack.pop()
        array.append([i, num])

# 괄호 인덱스의 모든 조합
for i in range(1, len(array)+1):
    for com in list(combinations(array, i)):
        cut = []
        result = []
        for c in com:
            x, y = c
            cut.append(x)
            cut.append(y)
        for d in range(len(data)):
            if d in cut:
                continue
            else:
                result.append(data[d])
        ans.append(''.join(result))

ans = list(set(ans))    # 중복제거

for a in sorted(ans):   # 사전순서로 출력
    print(a)