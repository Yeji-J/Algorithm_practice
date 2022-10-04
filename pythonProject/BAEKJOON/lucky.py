import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def lucky():
    idx = 0  # 화살표가 가리키는 칸 0부터 시작
    ch = []
    for _ in range(K):
        cnt, letter = input().split()
        idx = (idx + int(cnt)) % N  # 인덱스 초과하면 다시 0으로
        last = letter       # 기록된 마지막 문자

        if letter not in ch:        # 돌림판에 존재하지 않는 문자일 때
            if lst[idx] == '?':  # 해당 값이 '?'일 떄 (값이 없을 때)
                lst[idx] = letter  # 알파벳 넣기
                ch.append(letter)

            else:  # 해당 값이 '?'이 아닌데
                if lst[idx] != letter:  # 들어온 letter와 같지 않을 때 (충돌)
                    return '!'  # 느낌표 출력
        else:
            if lst[idx] != letter:
                return '!'

    return lst+[last]

N, K = map(int, input().split())    # N : 바퀴 칸 수    K : 회전수
lst = ['?'] * N
last = ''           # 마지막 문자

lucky_lst = lucky()     # 함수 실행 & 채워진 리스트

if lucky_lst != '!':
    end = lucky_lst.pop()

    std = 0         # 기준으로 출력
    for i in range(N):
        if lucky_lst[i] == end:
            std = i

    ans = lucky_lst[std+1:] + lucky_lst[:std+1]
    print("".join(ans[::-1]))
else:
    print(lucky_lst)