function solution(n) {
    let pattern = "수박";
    let result = pattern.repeat(n);
    return result.slice(0, n);
}