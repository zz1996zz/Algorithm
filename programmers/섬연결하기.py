def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    connect = set([costs[0][0]])
    while len(connect) < n:
        for s, e, c in costs:
            if s in connect and e in connect:
                continue
            if s in connect or e in connect:
                connect.add(s)
                connect.add(e)
                answer += c
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))