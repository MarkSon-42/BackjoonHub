import math

# 입력 받기
A, B = map(int, input().split())
C, D = map(int, input().split())

# 분수의 합 구하기
denominator = B * D
numerator = A * D + B * C

# 기약분수로 만들기
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

# 출력
print(numerator, denominator)