import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

# max index 구하는 함수
def getMaxIndex(days):
    max_idx = 0
    for i in range(1, len(days)):
        if days[max_idx] < days[i]:
            max_idx = i
    return max_idx


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    days = list(map(int, input().split()))
    sm = 0
    # days 원소 개수가 2이상일 때만
    while len(days) > 1:
        max_idx = getMaxIndex(days)                         # 최댓값 인덱스
        i =                     0                           # 리스트 첫 원소부터 시작
        while i < max_idx:                                  # 최댓값 인덱스보다 작을 때까지
            sm += days[max_idx] - days[i]                   # 이익 누적
            i += 1

        # 최댓값 인덱스를 넘긴다면 (최댓값 인덱스 이상)
        days = days[i+1:] # 다음 인덱스부터 슬라이싱으로 새로운 리스트 대입

    print(f'#{test_case} {sm}')



