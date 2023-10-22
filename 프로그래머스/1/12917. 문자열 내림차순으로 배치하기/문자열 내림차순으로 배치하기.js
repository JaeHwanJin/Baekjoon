function solution(s) {
    // var answer = s.split("").sort((a,b)=>a-b).reverse().join("")
    var answer = s.split('').sort().reverse().join('');
    return answer;
}