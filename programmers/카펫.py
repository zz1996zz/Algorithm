def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        a = yellow // i # a는 노란색 타일의 가로 개수
        b = (a+2) * (i+2) - yellow # b는 노란색을 제외한 갈색 타일의 수
        if yellow % i == 0 and b == brown:
            answer = [a+2, i+2]
            break
    return answer