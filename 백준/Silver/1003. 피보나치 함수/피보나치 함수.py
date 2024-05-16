T = int(input())
for _ in range(T):
    N = int(input())
    zero_call, one_call = 1, 0 

    for _ in range(N):
        zero_call, one_call = one_call, zero_call + one_call 

    print(zero_call, one_call)