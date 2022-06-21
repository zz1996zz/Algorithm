# import sys
# sys.stdin = open("input.txt", "rt")
#
# N = int(sys.stdin.readline())
# scores = list(map(int, sys.stdin.readline().split()))
# result, avg = [], 0
#
# avg = round(sum(scores)/len(scores))
#
# for i in range(len(scores)):
#     num = abs(avg-scores[i])
#     if len(result) == 0:
#         result.append([scores[i], num, i+1])
#     # 차이값이 작거나 같을 경우
#     elif result[0][1]>=num:
#         if result[0][1] > num:
#             result[0] = [scores[i], num, i+1]
#         # 차이값이 같은데 점수가 높거나 같을 경우
#         elif result[0][1] == num and result[0][0] <= scores[i]:
#             if result[0][0] < scores[i]:
#                 result[0] = [scores[i], num, i+1]
#             # 점수가 같은데 번호가 더 빠를 경우
#             elif result[0][0] == scores[i] and result[0][2] > i:
#                 result[0] = [scores[i], num, i+1]
#             else:
#                 continue
# print(avg, result[0][2])


import sys
sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
avg = int(sum(scores)/len(scores) + 0.5)
min = 2147000000

for idx, val in enumerate(scores):
    tmp = abs(avg-val)
    if tmp < min:
        min = tmp
        score = val
        answer = idx+1
    elif tmp == min:
        if score < val:
            score = val
            answer = idx+1
print(avg, answer)