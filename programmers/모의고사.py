def solution(answers):
    answer = []
    a, b, c = 0, 0, 0
    x, y, z = 0, 0, 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in answers:
        if a > 4: a = 0
        if b > 7: b = 0
        if c > 9: c = 0
        if one[a] == i:
            x += 1
            a += 1
        if two[b] == i:
            y += 1
            b += 1
        if three[c] == i:
            z += 1
            c += 1

    k = max(x, y, z)
    for i, j in enumerate([x, y, z], start=1):
        if k == j:
            answer.append(i)

    return answer

print(solution([1, 3, 2, 4, 2]))