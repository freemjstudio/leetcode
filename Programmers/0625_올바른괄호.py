# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):

    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            # )
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            elif stack[-1] == ")":
                return False

    if len(stack) > 0:
        return False

    return True