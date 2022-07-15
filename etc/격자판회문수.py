import sys

sys.stdin = open("input.txt", "rt")


def palindrome(word):
    global answer
    word = ''.join(word)
    word_reverse = ''.join(reversed(word))
    if word == word_reverse:
        answer += 1
    return


N = 7
plate = [list(map(str, input().split())) for _ in range(N)]
answer = 0

for i in range(N):
    palindrome(plate[i][0:5])
    palindrome(plate[i][1:6])
    palindrome(plate[i][2:7])

    tmp = list(zip(*plate))
    palindrome(tmp[i][0:5])
    palindrome(tmp[i][1:6])
    palindrome(tmp[i][2:7])

print(answer)