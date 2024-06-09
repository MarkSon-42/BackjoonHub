// function solution(n) {
//     let sum = 0;
//     let strN = String(n);

//     for (let i = 0; i < strN.length; i++) {
//         sum += Number(strN[i]);
//     }

//     return sum;
// }


function solution(n) {
    let sum = 0;
    let strN = String(n);
    
    for (let i = 0; i < strN.length; i++) {
        sum += Number(strN[i])
    }
    
    return sum;
}