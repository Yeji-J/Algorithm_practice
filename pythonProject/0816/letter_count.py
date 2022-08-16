import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    str_dict = dict()
    # str1 문자 딕셔너리 생성
    for letter1 in str1:
        str_dict[letter1] = 0
    # str2에서 해당 문자 개수 카운팅
    for letter2 in str2:
        if letter2 in str_dict:
            str_dict[letter2] += 1

    ans = 0
    for value in str_dict.values():
        if value > ans:
            ans = value

    print(f'#{test_case} {ans}')

# 딕셔너리를 이용할 수 없는 언어라면 ASCII(0~127) 카운팅 배열 활용