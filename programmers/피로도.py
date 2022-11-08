from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for p in permutations(dungeons, len(dungeons)):
        pirodo, cnt = k, 0
        for dungeon in p:
            if pirodo >= dungeon[0]:
               pirodo -= dungeon[1]
               cnt += 1
        answer = max(answer, cnt)
    return answer