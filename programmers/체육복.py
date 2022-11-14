def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)

    for i in _reserve:
        if i - 1 in _lost:
            _lost.remove(i - 1)
        elif i + 1 in _lost:
            _lost.remove(i + 1)
    return n - len(_lost)

print(solution(	5, [2, 4], [3]))