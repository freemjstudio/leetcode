def solution(N, number):
    # 같은 경우
    if N == number:
        return 1

    dp = [[0], [N]]  # N을 i 번 사용한 경우 , 계산한 결과 값 저장
    for i in range(2, 9):
        temp_dp = set()  # N을 i번 쓰는 경우 임시 저장 테이블
        temp_dp.add(int(str(N) * i))  # ex. 5 -> 55
        # 사칙연산

        for x in dp[i - 1]:
            temp_dp.add(x + N)
            temp_dp.add(x - N)
            temp_dp.add(x * N)

            if x != 0:
                temp_dp.add(x / N)

        if number in temp_dp:
            return i
        dp.append(list(temp_dp))
    # 8개 이하에 number 값이 없는 경우
    return -1