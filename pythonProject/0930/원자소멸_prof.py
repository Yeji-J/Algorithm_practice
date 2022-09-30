import sys
sys.stdin = open("input.txt", "r")

# 주어진 좌표에서 나가면 영원히 충돌할 일 없음
# 0.5초씩 이동 => 좌표*2 => 이동은 1칸씩

# 4001번 loop 이동
# [1] 1칸 이동처리
# [2] 같은 좌표인 경우 처리 - 중복여부 체크만 (i, j 정렬해 처리)
# [3] 동일좌표 삭제 + 에너지 누적

di = (1, -1, 0, 0)
dj = (0, 0, -1, 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # [0] 각 원자 i, j 좌표 * 2 => 1씩 이동
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2

    ans = 0
    # 4001번 루프: 가장 멀리 있는 원자가 충돌할 경우
    for _ in range(4001):
        # [1] 좌표 1칸 이동 (j, i)
        for i in range(len(arr)):
            arr[i][0] += dj[arr[i][2]]
            arr[i][1] += di[arr[i][2]]

        # [2] 같은 좌표인 경우 delLst에 추가
        v = []
        delLst = set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj, ci) not in v:
                v.append((cj,ci))
            else:
                delLst.add((cj,ci))     # set이니까 중복 제거

        # [3] delLst에 있는 원자 삭제 및 에너지 누적
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in delLst:
                ans += arr[i][3]
                arr.pop(i)      # 끝에서부터 pop이라 인덱스에 문제 없음!

        for i in range(1, len(arr)):
            if arr[i][2] != arr[i - 1][2]:
                break
        else:
            break  # 모든 원자의 방향이 같음

        if len(arr) < 2:
            break

    print(f'#{tc} {ans}')