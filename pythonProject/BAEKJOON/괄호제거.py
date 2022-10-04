import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')


st = input()
# 열린괄호(뒤에서부터 pop), 닫힌괄호(앞에서부터 pop)
lst1, lst2 = [], []
lst = []
for k in range(len(st)):
    if st[k] == '(':
        if len(lst1) > 0 and len(lst1) == len(lst2):
            while lst1:
                lst.append((lst1.pop(), lst2.pop(0)))
        lst1.append(k)
    elif st[k] == ')':
        lst2.append(k)

if lst1:
    while lst1:
        lst.append((lst1.pop(), lst2.pop(0)))

# 조합
res = []
for i in range(1, 2 ** len(lst)):
    idx = []
    for j in range(len(lst)):
        if 1 & (i >> j):
            idx += [*lst[j]]
    res.append(idx)

# print(res)
ans = []
for m in res:
    tmp = ''
    for x in range(len(st)):
        if x not in m:
            tmp += st[x]
    ans.append(tmp)

# 중복제거
ans = list(set(ans))
ans.sort()

# 출력
for n in ans:
    print(n)
