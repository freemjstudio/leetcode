
def solution(name):
    answer = 0
    n = len(name)

    # 상 / 하 비교 하여 mininum 값 구하기
    # Z 의 경우 COUNT 1로 취급해야 함
    left, right = 0, 0

    for i in range(n):
        m = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        right += m
        print(i, name[i], ord(name[i]), m)
        if name[i:] == ( n -i) * 'A':
            print("right")
            print(name[i:])
            break

        right += 1

    # 첫번쨰 위치에서 바로 왼쪽으로 이동하는 경우 처리
    print()
    for j in range(n, -1, -1):
        m = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        left += m
        print(i, name[i], ord(name[i]), m)
        if name[:i] == ( n -i) * 'A':
            print("left")
            print(name[:i])
            break
        left += 1


    # 예외 BAA, AAB
    # AAA -> JAN A->J, A, A->N
    # AAAAAA -> JEROEN 이 경우는 어처피 좌우 상관 없음


    # 좌 / 우 비교
    answer = min(left, right)
    return answer