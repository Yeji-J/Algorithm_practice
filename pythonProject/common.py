import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in (1, T+1):
#     N = int(input())
#     nums = list(map(int, input()))
#
#     cnts = [0] * 10
#
#     for n in nums:
#         cnts[n] += 1
#
#
#     idx = 0
#     for i in range(1, 10):
#         # 개수가 같을 땐 더 큰 숫자 출력하기 위해 <=
#         if cnts[idx] <= cnts[i]:
#             idx = i
#
#     print(f'#{test_case} {idx} {cnts[idx]}')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input()))
    # counts 배열 생성
    #     # 0 ~ 9
    cnts = [0] * 10
    # cnts 인덱스에 숫자 개수 넣기
    for n in nums:
        cnts[n] += 1

    # 인덱스 초기화
    idx = 0
    for i in range(1, 10):
        if cnts[idx] <= cnts[i]:
            idx = i
    print(f'#{test_case} {idx} {cnts[idx]}')