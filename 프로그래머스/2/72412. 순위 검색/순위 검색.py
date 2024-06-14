from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in info:
        i = i.split()
        conditions = i[:-1]
        score = int(i[-1])
        for j in range(5):
            for c in combinations(conditions, j):
                info_dict["".join(c)].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split(" ")
        q_score = int(q[-1])
        q = q[:-1]

        q = [i for i in q if i != 'and' and i != '-']
        q = "".join(q)

        if q in info_dict:
            scores = info_dict[q]
            answer.append(len(scores) - bisect_left(scores, q_score))
        else:
            answer.append(0)

    return answer