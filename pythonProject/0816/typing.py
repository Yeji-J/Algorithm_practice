import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    A, B = map(list, input().split())
    cnts = 0
    # 인덱스 0부터 len(A) - len(B)까지
    for i in range(len(A)-len(B)+1):
        lst = []
        # B의 글자수만큼 단어 끊기
        for j in range(i, i+len(B)):
            lst.append(A[j])
        # 해당 단어가 B와 동일하다면
        if lst == B:
            cnts += 1
            for j in range(i, i+len(B)):
                A[j] = 0
    for letter in A:
        if letter != 0:
            cnts += 1

    print(f'#{test_case} {cnts}')
