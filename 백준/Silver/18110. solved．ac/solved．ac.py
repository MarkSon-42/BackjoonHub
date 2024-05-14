import sys

def round_up(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
else:
    opinions = []
    
    for i in range(n):
        opinions.append(int(sys.stdin.readline().rstrip()))
        
    opinions.sort()
    trim_count = round_up(n * 0.15)
    
    trimmed_opinions = opinions[trim_count:n-trim_count]
    average_difficulty = round_up(sum(trimmed_opinions)/len(trimmed_opinions))
    
    print(average_difficulty)