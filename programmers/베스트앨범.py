def solution(genres, plays):
    answer = []
    album = sorted(list(zip(genres, plays)), reverse = True)
    album_dict = dict()
    count_dict = dict()
    for key, value in album:
        if key not in album_dict:
            album_dict[key] = value
            count_dict[key] = 0
        else:
            album_dict[key] += value
    sorted_dict = sorted(album_dict.items(), key = lambda item: item[1], reverse = True)
    for key, value in sorted_dict:
        for k, v in album:
            if key != k or count_dict[k] == 2:
                continue
            n = plays.index(v)
            answer.append(n)
            plays[n] = -1
            count_dict[k] += 1
    return answer