function solution(phone_number) {
    let len = phone_number.length;
    let hidePart = '*'.repeat(len - 4);
    let showPart = phone_number.slice(-4);
    return hidePart + showPart;
}