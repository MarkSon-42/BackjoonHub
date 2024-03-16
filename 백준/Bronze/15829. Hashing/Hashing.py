MODULUS = 1234567891
BASE = 31

length = int(input())
input_string = input()
hash_value = 0

for i in range(len(input_string)):
    char_value = ord(input_string[i]) - ord('a') + 1
    hash_value += char_value * (BASE ** i)

print(hash_value % MODULUS)