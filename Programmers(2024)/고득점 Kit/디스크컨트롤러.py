import heapq


def solution(jobs):
    answer = 0
    disk = []
    N = len(jobs)
    done = 0  # 처리된 task 수
    time = 0
    last = -1
    while done < N:

        for job in jobs:
            if last < job[0] <= time:
                heapq.heappush(disk, [job[1], job[0]])
            # 소요시간 짧은 순으로 정렬하기

        if disk:
            duration, start = heapq.heappop(disk)
            last = time  # 작업이 끝난 시간
            time += duration
            answer += (time - start)

            done += 1
        else:

            # 처리가능하면 처리하고 안되면 다시 push 하기
            time += 1

    return int(answer / N)