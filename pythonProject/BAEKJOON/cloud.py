import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

H, W = map(int, input().split())
arr = [input().split() for _ in range(H)]
stk = []
res = []

for lst in arr:
    for ch in lst:
        if not stk:             # 스택이 비었다면
            stk.append(ch)      # 무조건 추가

        if ch != 'c':           # 구름이 아니라면
            stk.append(ch)      # 무조건 추가

        else:                           # 구름일 때
            if ch not in stk:           # 스택 안에 또다른 구름이 없으면 (첫 구름이면)
                while not stk:          # 스택 안 모든 데이터를 빼고
                    stk.pop(0)
                    res.append(-1)      # -1로 추가

            else:                       # 스택 안에 또다른 구름이 있으면
                stk.pop(0)              # 구름을 빼고
                res.append(0)
                if stk:                     # 구름을 뺀 스택에 데이터가 있다면
                    i = 0
                    while not stk:          # 스택이 빌 때까지
                        stk.pop(0)          # 빼고 i 증가하며 추가
                        res.append(i)
                        i += 1
                    stk.apppend(ch)         # 구름 추가

    if stk:
        stk.pop(0)  # 구름 빼고
        res.append(0)
        i = 0
        while not stk:
            stk.pop(0)
            res.append(i)
            i += 1

    print(res)