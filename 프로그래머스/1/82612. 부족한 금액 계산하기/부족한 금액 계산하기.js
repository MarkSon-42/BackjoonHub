function solution(price, money, count) {
    let total = 0;

    for (let i = 1; i <= count; i++) {
        total += price * i;
    }

    let result = money - total;

    return result >= 0 ? 0 : -result;
}