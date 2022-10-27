def solution(bridge_length, weight, truck_weights):
    answer = 0
    s = len(truck_weights)
    ing = []
    cnt = 0
    while cnt < s:
        answer += 1

        if len(ing) != 0 and ing[0][1] == bridge_length:
            ing.pop(0)
            cnt += 1

        if len(ing) != 0:
            for i in range(len(ing)):
                ing[i][1] += 1

        if len(truck_weights) != 0 and weight >= sum(w for w, t in ing) + truck_weights[0]:
            ing.append([truck_weights.pop(0), 1])

    return answer
