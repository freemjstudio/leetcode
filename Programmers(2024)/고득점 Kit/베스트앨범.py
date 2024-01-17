from collections import defaultdict


def solution(genres, plays):
    answer = []
    n = len(genres)
    hash_map = defaultdict(int)  # -> 조건 1: 속한 노래가 많이 재생된 장르
    hash_song = defaultdict(list)  # -> 장르 내에서 많이 재생된 노래 classic : [(500, 0), (150, 2), ...]
    for i in range(n):
        hash_map[genres[i]] += plays[i]
        hash_song[genres[i]].append((plays[i], i))
    gen_arr = sorted(list(hash_map.items()), reverse=True, key=lambda item: item[1])
    for gen_item in gen_arr:
        gen = gen_item[0]
        sorted_song = sorted(hash_song[gen], reverse=True, key=lambda item: (item[0], -item[1]))
        for i in range(len(sorted_song)):
            if i >= 2:
                break
            answer.append(sorted_song[i][1])

    return answer


'''
다른 풀이 
'''

