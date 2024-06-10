function solution(arr) {
    let min = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }

    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== min) {
            result.push(arr[i]);
        }
    }

    if (result.length === 0) {
        return [-1];
    } else {
        return result;
    }
}