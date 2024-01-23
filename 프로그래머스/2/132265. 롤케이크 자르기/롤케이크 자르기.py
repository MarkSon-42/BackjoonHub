def solution(toppings):
    # 공정한 분배 횟수를 초기화합니다.
    fair_division_count = 0

    # 왼쪽 케이크 부분의 토핑을 세는 사전을 초기화합니다.
    left_cake_toppings = {}

    # 왼쪽 케이크 부분의 토핑을 세기
    for topping in toppings:
        if topping in left_cake_toppings:
            left_cake_toppings[topping] += 1
        else:
            left_cake_toppings[topping] = 1

    # 오른쪽 케이크 부분의 토핑을 세는 사전을 초기화합니다.
    right_cake_toppings = {}

    # 오른쪽 케이크 부분의 토핑을 세고 공정한 분배를 확인합니다.
    for topping in toppings:
        # 양쪽 부분의 고유한 토핑 수가 동일하면 공정한 분배 횟수를 증가시킵니다.
        if len(right_cake_toppings) == len(left_cake_toppings):
            fair_division_count += 1

        # 토핑을 오른쪽 케이크 부분에 추가합니다.
        if topping not in right_cake_toppings:
            right_cake_toppings[topping] = 1

        # 왼쪽 케이크 부분에서 토핑을 제거합니다.
        left_cake_toppings[topping] -= 1

        # 왼쪽 케이크 부분에 이 토핑이 더 이상 없으면 사전에서 제거합니다.
        if left_cake_toppings[topping] == 0:
            del left_cake_toppings[topping]

    # 공정한 분배 횟수를 반환합니다.
    return fair_division_count