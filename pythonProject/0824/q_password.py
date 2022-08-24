import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def createPw(arr1, arr2):
    cycle = 1   # 리스트 내 원소 다 돌았을 때 cycle == 1
    i = 1       # 1 ~ 5 마이너스
    while True:
        if cycle >= 1:
            arr1, arr2 = arr2, arr1

        for _ in range(N):
            if arr1:
                tmp = arr1.pop(0) - i      # arr1 첫 번째 원소에서 i만큼 빼기
                if tmp <= 0:                # 0보다 작다면
                    arr2.append(0)         # arr2 0을 추가하고
                    return arr1 + arr2    # 함수 종료

                else:                       # 0보다 크다면
                    arr2.append(tmp)       # arr2 그대로 추가

                i += 1                      # i 증가
                if i == 6:                  # 6이 되면 1로 초기화
                    i = 1

        cycle += 1          # 원소 다 돌았을 때  cycle +1


for _ in range(10):
    tc = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = []
    N = len(arr1)
    ans = createPw(arr1, arr2)
    print(f'#{tc}', *ans)