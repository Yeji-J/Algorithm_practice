import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())        # 후보 수
D = int(input())        # 다솜이 득표
rest = [int(input()) for _ in range(N-1)]       # 나머지 사람 수

if N == 1:              # 후보가 다솜이 1명일 때
    ans = 0

else:                   # 후보가 2명 이상일 때
    cnts = 0            # 표를 뺏은 횟수
    while True:
        if D > max(rest):           # 다솜이 표가 제일 클 때
            ans = cnts
            break

        else:                                   # 다솜이 표가 나머지보다 작거나 같을 때
            for i in range(N-1):
                if rest[i] == max(rest):        # 나머지 후보들 중 가장 높은 표를 가진 사람
                    rest[i] -= 1                # 표 하나 뺏고
                    D += 1                  # 다솜이한테 추가
                    cnts += 1
                    break
print(ans)