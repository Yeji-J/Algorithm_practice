import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def bg(i, k):
    global ans
    if i == k:
        r = 0
        t = 0
        if lst[0] == lst[1] and lst[1] == lst[2]:           # run 확인
            r += 1
        if lst[0] + 1 == lst[1] and lst[1] + 1 == lst[2]:   # triplet 확인
            t += 1
        if lst[3] == lst[4] and lst[4] == lst[5]:
            r += 1
        if lst[3] + 1 == lst[4] and lst[4]+ 1 == lst[5]:
            t += 1
        if t + r == 2:
            ans = 1
    else:
        for j in range(i, k):
            lst[i], lst[j] = lst[j], lst[i]     #  자리 바꾸고
            bg(i+1, k)                           # 다음 자리 바꾸러 가기
            lst[i], lst[j] = lst[j], lst[i]     # 다녀오면 원상복귀
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    ans = 0
    bg(0, len(lst)-1)

    print(f'#{tc} {ans}')