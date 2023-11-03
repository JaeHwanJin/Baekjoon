function solution(k, score) {
    var answer = [];
    var stack = [score[0]];
    for(let i=1; i<score.length; i++){
        var min = Math.min(...stack);
        if(stack.length<k){
            stack.push(score[i]);
        }
        else{
            if(score[i]>min){
                var idx = stack.indexOf(min)
                stack.splice(idx,1)
                stack.push(score[i])
            }
        }
        answer.push(min)
    }
    answer.push(Math.min(...stack))
    return answer;
}