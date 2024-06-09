function solution(arr) {
    let sum = 0;
    let len = arr.length
    for (let i = 0; i < len; i++) {
        sum += arr[i];
    }
    return sum / len;
}