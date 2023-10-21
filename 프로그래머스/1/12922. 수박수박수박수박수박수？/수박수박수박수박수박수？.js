function solution(n) {
    var answer = '';
    var word = "수박";

    if(n%2 === 0){
        answer = word.repeat(n/2)
    } else{
        answer = word.repeat(parseInt(n/2)) + "수"
    }
    return answer;
}