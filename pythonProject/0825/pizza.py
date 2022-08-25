import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())        # N: 화덕 크기 M: 피자 개수
    chs = list(map(int, input().split()))   # 치즈 리스트

    for i in range(M):          # 피자 인덱스와 함께 저장
        chs[i] = [chs[i], i+1]

    pizza = []          # 화덕 안 피자

    for _ in range(N):              # 화덕에 처음 집어 넣고
        pizza.append(chs.pop(0))

    while len(pizza) > 1:                # 화덕에 피자가 하나 남을 때까지

        tmp = pizza[0][0] // 2             # 피자 꺼내서 치즈 확인

        if tmp == 0:                    # 치즈 다 녹으면 꺼내기

            if chs:                     # 남아있는 피자 화덕에 추가
                pizza[0] = chs.pop(0)
            else:                       # 남아있는 게 없으면 그냥 꺼내기
                pizza.pop(0)

        else:                           # 치즈 다 안 녹음
            pizza[0][0] //= 2              # 반 녹은 치즈 양으로 초기화
            pizza.append(pizza.pop(0))      # 뒤로 보내기

    print(f'#{test_case} {pizza[0][1]}')