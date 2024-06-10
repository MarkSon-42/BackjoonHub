function solution(numbers) {
    let totalSum = 45;
    let numbersSum = numbers.reduce((a, b) => a + b, 0);
    return totalSum - numbersSum;
}