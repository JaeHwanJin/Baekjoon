function solution(answers) {
    var one = [1,2,3,4,5];
    var oneAnswer = 0;
    var two = [2,1,2,3,2,4,2,5];
    var twoAnswer = 0;
    var three = [3,3,1,1,2,2,4,4,5,5];
    var threeAnswer = 0;
    var result = [0,0,0];
    for(let i=0; i<answers.length; i++){
        if(answers[i]===one[i%5]){
            oneAnswer += 1;
            result[0]=oneAnswer
        }
        if(answers[i]===two[i%8]){
            twoAnswer += 1;
            result[1]=twoAnswer
        }
        if(answers[i]===three[i%10]){
            threeAnswer += 1;
            result[2]=threeAnswer
        }
    }
    var max = Math.max(...result);
    var answer = [];
    for(let j=0; j<result.length; j++){
        if(max===result[j]){
            answer.push(j+1)
        }
    }
    return answer;
}