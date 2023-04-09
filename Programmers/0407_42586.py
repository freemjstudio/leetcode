# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    stack = []
    N = len(progresses)
    for i in range(N):
        progress = 100 - progresses[i]
        if progress % speeds[i] != 0:
            day = progress // speeds[i] + 1
            stack.append(day)
        else:
            day = progress // speeds[i]
            stack.append(day)
    print(stack)

    return answer