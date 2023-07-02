def solution(N, number):
    # 같은 경우
    if N == number:
        return 1

    dp = []  # N을 i 번 사용한 경우 , 계산한 결과 값 저장
    for i in range(1, 9):
        temp_dp = set()  # N을 i번 쓰는 경우 임시 저장 테이블
        temp_dp.add(int(str(N) * i))  # ex. 5 -> 55

        # 사칙연산
        for j in range(i - 1):
            for x in dp[j]:  # i개 이전의 dp 값에서 꺼내오기
                for y in dp[-j - 1]:  #
                    temp_dp.add(x + y)
                    temp_dp.add(x - y)
                    temp_dp.add(x * y)

                    if y != 0:
                        temp_dp.add(x / y)

        if number in temp_dp:
            return i
        dp.append(temp_dp)
    # 8개 이하에 number 값이 없는 경우
    return -1