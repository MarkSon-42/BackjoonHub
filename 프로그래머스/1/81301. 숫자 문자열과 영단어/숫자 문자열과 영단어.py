def solution(s):
    words_to_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    result = ''
    word = ''
    for char in s:
        if char.isdigit():
            result += char
        else:
            word += char
            if word in words_to_number:
                result += words_to_number[word]
                word = ''
    return int(result)