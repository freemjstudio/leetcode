
def solution(name):
    answer = 0
    n = len(name)
    steps = n # 좌우 움직이기

    # 상 / 하 비교 하여 mininum 값 구하기
    # Z 의 경우 COUNT 1로 취급해야 함

    for i in range(n):
        m = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        answer += m

        # 연속된 A 찾기

        # B B A A A
        pointer = i+ 1
        while pointer < n and name[pointer] == 'A':
            pointer += 1

        # 왼쪽 오른쪽 비교
        steps = min(steps, i + 2 * (n - pointer), 2 * i + (n - pointer))

    answer += steps

    return answer