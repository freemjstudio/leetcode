from itertools import combinations

def solution(clothes):
    answer = 0
    # 1개 , 2 개 , .. N 개 입는 조합
    d = {}

    for item in clothes:
        v, k = item
        if k in d.keys():
            d[k].append(v)
        else:
            d[k] = [v]
    categories = list(d.keys())

    for i in range(1, len(categories) + 1):
            comb = combinations(categories, i)
            for com in comb:
                temp = 1
                for c in com:
                    temp *= len(d[c])
                answer += temp

    return answer