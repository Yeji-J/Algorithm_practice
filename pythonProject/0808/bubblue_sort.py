def bubbleSort(A, N):
    # A : 정렬할 리스트
    # N : 리스트 원소의 개수
    for i in range(N-1, 0, -1): #원소 범위 줄여가면서
        for j in range(0, i):
            if A[j] > A[j+1]: # 크기 비교
                A[j], A[j+1] = A[j+1], A[j] # 크기가 큰 애들 앞 자리로 교환