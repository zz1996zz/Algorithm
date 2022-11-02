def solution(numbers):
    answer = ''
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    for x in numbers:
        answer += x
    if answer[0] == "0":
        return "0"
    return answer