import math

def solution(progresses, speeds):
    answer = []
    period = []
    count = 1
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        period.append(day)
    max_num = period.pop(0)
    for i in period:
        if max_num < i:
            max_num = i
            answer.append(count)
            count = 1
            continue
        count += 1
    answer.append(count)
    return answer