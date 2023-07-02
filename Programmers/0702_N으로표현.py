# https://school.programmers.co.kr/learn/courses/30/lessons/42895


def recur(x, count, number, N):
    if count > 8:
        return

    if x == number:
        return count
    recur(x + N, count + 1, number, N)
    recur(x - N, count + 1, number, N)
    recur(x * N, count + 1, number, N)
    recur(x / N, count + 1, number, N)

    # 5 -> 55 로 만들기
    if isinstance(x, int):
        nx = str(x) + str(N)
        recur(int(nx), count + 1, number, N)


def solution(N, number):
    answer = 9
    if N == number:
        return 1

    answer = min(recur(N, 1, number, N), answer)
    return answer