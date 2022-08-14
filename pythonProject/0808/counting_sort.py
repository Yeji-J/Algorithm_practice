# 보통 카운팅 배열은 100까지만 씀
# 배열을 하나 더 만들어서 해당 인덱스 값 카운팅 누적

A = [0, 4, 1, 3, 1, 2, 4, 1] # 0 ~ 4까지의 정수
cnts_A = [0] * 5

# 각 원소의 빈도수 구하기
for i in range(len(A)):
    cnts_A[A[i]] += 1
print(cnts_A) # [1, 3, 1, 1, 2]

# 원소의 개수 누적하기
for j in range(1, len(cnts_A)):
    cnts_A[j] = cnts_A[j-1] + cnts_A[j]
print(cnts_A) # [1, 4, 5, 6, 2]

# Q. 2 ~ 4까지 원소의 개수는 ?
print(cnts_A[4] - cnts_A[1]) # 4개

# Counting Sort Process
tmp = [0] * len(A)

for k in range(len(A)-1, 0, -1): # 마지막 원소부터 시작
    cnts_A[A[k]] -= 1 # 원소합 누적한 리스트에서 해당 원소 누적 합 -1
    tmp[cnts_A[A[k]]] = A[k] # 누적 합에서 하나를 제했으니, 해당 원소 temp[누적합인덱스]에 저장
print(tmp) # 크기 순 정렬 완료 :)