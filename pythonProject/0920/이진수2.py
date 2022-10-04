import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# [1] 2를 "곱한 후" 정수와 소수 부분 분리
# [2] 다시 소수 부분에 2를 곱한 후 분리
# [3] 소수 부분 0이되면 종료

T = int(input())
for tc in range(1, T + 1):
    num = float(input())

    ans = ''
    while num:              # num== 0 stop

        ans += str(int(num*2))      # 정수 부분 저장
        num = num*2 - int(num*2)    # 실수 부분으로 초기화

        if len(ans) > 12:           # 길이가 12를 넘기면
            ans = 'overflow'
            break

    print(f'#{tc} {ans}')