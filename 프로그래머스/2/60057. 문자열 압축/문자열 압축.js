function solution(s) {
    let answer = s.length;

    for (let i = 1; i <= Math.floor(s.length / 2); i++) {
        let compressed = "";
        let prev = s.substring(0, i);
        let count = 1;

        for (let j = i; j < s.length; j += i) {
            let substr = s.substring(j, j + i);

            if (prev === substr) {
                count++;
            } else {
                compressed += count > 1 ? count + prev : prev;
                prev = substr;
                count = 1;
            }
        }

        compressed += count > 1 ? count + prev : prev;
        answer = Math.min(answer, compressed.length);
    }

    return answer;
}