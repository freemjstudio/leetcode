'''
Lv.2	72414	광고 삽입
Lv.2	17684	압축
14499	주사위 굴리기
'''


def solution(msg):
    answer = []
    word_num = 27
    word_dict = {chr(i): (i - 64) for i in range(65, 91)}

    n = len(msg)
    start = 0
    while True:
        if start == n - 1:
            break
        for end in range(n - 1, start, -1):
            if msg[start:end + 1] in word_dict:
                answer.append(word_dict[msg[start:end + 1]])
            else:  # 없는 경우
                if end == start:  # 마지막일 때
                    word_dict[msg[start]] = word_num
                    word_num += 1
                else:
                    continue

    return answer