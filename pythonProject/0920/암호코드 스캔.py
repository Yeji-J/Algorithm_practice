import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

pwDic = {'211':'0', '221':'1', '122':'2', '411':'3', '231':'5', '114':'6', '312':'7', '213':'8', '112':'9'}
Hdic = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 세로  M: 가로
    lst = list(input().strip('0') for _ in range(N))

    # 암호문 저장
    st_lst = []
    for st in lst:                                          # 암호문 각 줄에 대해
        tmp = []
        tst = ''
        for i in range(len(st)):
            # tst에 값이 있고, '0'을 만났을 때 혹은 마지막 문자일 때
            if tst and st[i] == '0' or i == len(st) - 1:
                tmp.append(tst)                         # tst에 저장된 값 tmp에 저장
                tst = ''                                # tst 초기화

            elif st[i] != '0':                          # '0'이 아니라면 계속 추가
                tst += st[i]

        if tmp and tmp not in st_lst:                   # st_lst에 없는 값이라면 최종적으로 저장
            st_lst.append(tmp)
    print(st_lst)

    # 2진수 변환
    res = []
    for lst in st_lst:
        tmp2 = []
        for hex in lst:
            tmp3 = ''
            for ch in hex:
                tmp3 += Hdic[ch]
            tmp2.append(tmp3)
        res.append(tmp2)
    print(res)

    # 비율
    cnts = []
    for lst in res:
        tmp = []
        for pw in lst:
            old = 0
        for j in range(len(pw)):
            if pw[old] != pw[j]:
                tmp.append(j-old)
                old = j
        cnts.append(tmp)

    print(cnts)





    print()

