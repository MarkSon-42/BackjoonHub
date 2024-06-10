function solution(s, n) {
    let result = '';

    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ') {
            result += ' ';
        } else {
            let ascii = s[i].charCodeAt(0);
            if (ascii >= 65 && ascii <= 90) {
                result += String.fromCharCode((ascii - 65 + n) % 26 + 65);
            } else if (ascii >= 97 && ascii <= 122) {
                result += String.fromCharCode((ascii - 97 + n) % 26 + 97);
            }
        }
    }

    return result;
}