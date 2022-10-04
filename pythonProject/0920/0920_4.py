import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# 암호 끝 index
def end():
    global e
    for j in range(M-1, -1, -1):
        if lst[j] == '1':
            e = j
            return e


dct = {
    '0':'0001101', '1':'0011001', '2':'0010011', '3':'0111101', '4':'0100011', '5':'0110001', '6':'0101111', '7':'0111011', '8':'0110111', '9':'0001011'
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 세로 M: 가로
    arr = list(input() for _ in range(N))

    lst = 0
    for i in range(N):
        if '1' in arr[i]:
            lst = arr[i]
            break

    # 암호 시작위치
    ans = []
    e = 0
    end()

    # 암호 추출
    res = []
    for m in range(e-55, e+1, 7):
        tmp2 = lst[m:m+7]
        for n in range(10):
            if tmp2 == dct[str(n)]:
                res.append(n)

    # 유효성 검사
    odd = even = 0
    for k in range(len(res)-1):     # 검증코드 전까지
        if k % 2:               # 짝수자리(index 고려)
            even += res[k]
        else:
            odd += res[k]       # 홀수자리(index 고려)

    ans = 0
    pw = odd * 3 + even + res[-1]
    if pw % 10 == 0:        # 10의 배수라면
        ans = sum(res)

    print(f'#{tc} {ans}')






