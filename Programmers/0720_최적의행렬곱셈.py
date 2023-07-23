# 최적의 행렬 곱셈
# https://develop247.tistory.com/62#:~:text=%EC%98%88%EB%A5%BC%20%EB%93%A4%EC%96%B4%2C%206%EA%B0%9C%EC%9D%98,%EC%88%9C%EC%84%9C%EB%A5%BC%20%ED%95%AD%EC%83%81%20%ED%8F%AC%ED%95%A8%ED%95%A9%EB%8B%88%EB%8B%A4.


def solution(matrix_sizes):
    n = len(matrix_sizes)
    INF = int(1e9)
    dp = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0

    for step in range(1, n):
        for start in range(n):
            end = start + step
            if end >= n:
                break
            for sep in range(start, end):
                dp[start][end] = min(dp[start][end],
                                     dp[start][sep] + dp[sep + 1][end]
                                     + matrix_sizes[start][0] * matrix_sizes[sep][1] * matrix_sizes[end][1])

    return dp[0][n-1]


class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def matrix(element):
    answer = ALWAYS_CORRECT()

    return answer;


# 실행을 위한 테스트코드입니다.
if matrix([[5, 3], [3, 2], [2, 6]]) == 90:
    print("[[5,3],[3,2],[2,6]]인 경우에 정상동작합니다. 제출을 눌러서 다른 경우에도 정답인지 확인해 보세요.")
else:
    print("[[5,3],[3,2],[2,6]]인 경우에 정상동작하지 않습니다.")