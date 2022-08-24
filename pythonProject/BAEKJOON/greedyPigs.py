import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def feeding(lst1, lst2):
    global days
    if sum(lst1) > N:           # 처음부터 사료가 부족하면 종료
        return days
    else:
        while True:             # 다음날부터 계산
            days += 1                   # 하루 추가
            lst1, lst2 = lst2, lst1     # 리스트 번갈아가며 사용
            food = N                    # 하루마다 공급되는 사료

            # 돼지 사료 계산
            for i in range(6):
                lst1[i] = lst2[i] + lst2[(i+1) % 6] + lst2[(i+5) % 6] + lst2[(i+3) % 6]
            # 사료가 부족하면 함수 종료
            if sum(lst1) > food:
                return days


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = [0] * 6
    days = 1
    print(feeding(lst1, lst2))

