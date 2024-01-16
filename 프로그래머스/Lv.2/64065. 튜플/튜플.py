from collections import Counter

def solution(s):
    word_list = list(map(int, s.replace("}", "").replace("{", "").split(",")))
    count_dict = Counter(word_list).most_common()
    answer = [item[0] for item in count_dict]
    return answer