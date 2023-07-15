def solution(play_time, adv_time, logs):
    answer = ''  # min value

    if play_time == adv_time:
        return '00:00:00'

    start_points = []
    logs.sort()
    for log in logs:
        s, e = log.split("-")
        start_points.append(s)

    return answer