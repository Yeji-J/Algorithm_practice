<<<<<<< HEAD
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
=======
import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

st = input()
# 열린괄호(뒤에서부터 pop), 닫힌괄호(앞에서부터 pop)
lst1, lst2 = [], []

for k in range(len(st)):
    if st[k] == '(':
        lst1.append(k)
    elif st[k] == ')':
        lst2.append(k)

# 괄호 짝 인덱스
lst = []
for _ in range(len(lst1)):
    lst.append((lst1.pop(), lst2.pop(0)))

# 조합
res = []
for i in range(1, 2 ** len(lst)):
    idx = []
    for j in range(len(lst)):
        if 1 & (i >> j):
            idx += [*lst[j]]
    res.append(idx)
print(res)
ans = []
for m in res:
    tmp = ''
    for x in range(len(st)):
        if x not in m:
            tmp += st[x]
    ans.append(tmp)

ans.sort()
# 출력
for n in ans:
    print(n)
>>>>>>> d7f176263f59e12ff0945e93a117192ccbe47819
