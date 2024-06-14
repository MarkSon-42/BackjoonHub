def solution(friends, gifts):

    gift_map = {}
    given_map = {}
    received_map = {}
    answer_map = {}

    for f1 in friends:
        inner_gift_map = {}
        for f2 in friends:
            if f1 == f2:
                continue
            inner_gift_map[f2] = 0
        gift_map[f1] = inner_gift_map
        given_map[f1] = 0
        received_map[f1] = 0
        answer_map[f1] = 0

    for gift in gifts:
        given, received = gift.split()
        gift_map[given][received] += 1
        given_map[given] += 1
        received_map[received] += 1

    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            a = friends[i]
            b = friends[j]
            a_cnt = gift_map[a][b]            
            b_cnt = gift_map[b][a]
            
            if a_cnt > b_cnt:
                answer_map[a] += 1
            elif a_cnt < b_cnt:
                answer_map[b] += 1
            else:
                a_value = given_map[a] - received_map[a]
                b_value = given_map[b] - received_map[b]
                
                if a_value > b_value:
                    answer_map[a] += 1
                elif a_value < b_value:
                    answer_map[b] += 1
                    
    return max(answer_map.values())