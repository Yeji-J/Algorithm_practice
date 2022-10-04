import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
switch = list(map(int, input().split()))
ppl = []

for _ in range(int(input())):
    ppl.append(list(map(int, input().split())))

for one in ppl:
    # 남학생일 때
    if one[0] == 1:
        for i in range(N):
            if (i+1) % one[1] == 0:             # 스위치 번호(인덱스 + 1)가 배수면
                if switch[i] == 0:              # 스위치의 ON / OFF
                    switch[i] = 1
                else:
                    switch[i] = 0
    # 여학생일 때
    else:
        idx = one[1] - 1                # 인덱스 0부터 시작이니까

        if switch[idx] == 0:            # 자기 자신 ON/ OFF
            switch[idx] = 1
        else:
            switch[idx] = 0

        # 옆으로 뻗어나가기
        k = 1                   # 양 옆 인덱스 설정
        while True:
            left, right = idx - k, idx + k                  # 인덱스 1씩 옆으로

            if 0 <= left < N and 0 <= right < N:            # 인덱스가 범위 내에 있을 때

                if switch[left] == switch[right]:           # 양 옆 값이 같으면
                    if switch[left] == 0:                   # ON / OFF
                        switch[left], switch[right] = 1, 1
                    else:
                        switch[left], switch[right] = 0, 0
                else:                                       # 양 옆 값이 다르면 종료
                    break
            else:                                           # 인덱스 out of range 종료
                break
            k += 1

# 20개씩 나눠서 출력
for x in range(0, N, 20):
    print(*switch[x:x+20])


