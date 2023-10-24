function solution(n) {
    var answer = 0;
    var lst = [];
    var newNum = n;
    while(true){
        lst.push(newNum%3)
        newNum = Math.floor(newNum/3)
        if(newNum===0){
            const result = lst.reverse().join("")
            for(let i=0; i<result.length; i++){
                answer += result[i] * 3**i
            }
            break;
        }
    }
    return answer;
}