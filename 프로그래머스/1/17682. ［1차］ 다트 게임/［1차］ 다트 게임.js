function solution(dartResult) {
    var score = 0;
    var answer = [];
    var num = 0;
    for(let i=0; i < dartResult.length; i++){
        if(!isNaN(dartResult[i])){
            if(dartResult[i] == 1 && dartResult[i+1] == 0){
                num = 10;
                i++;
        }else{
            num = Number(dartResult[i]);
        }
            
        }
        else{
            if(dartResult[i] === "S"){
                answer.push(num);
            }else if(dartResult[i] === "D"){
                answer.push(Math.pow(num, 2));
            }else if(dartResult[i] === "T"){
                answer.push(Math.pow(num, 3));
            }else if(dartResult[i] === "*"){
                answer[answer.length - 1] *= 2;
                answer[answer.length - 2] *= 2;
            }else if(dartResult[i] === "#"){
                answer[answer.length - 1] *= -1;
            }
        }
        console.log(i, answer)
    }
    const result = answer.reduce((sum, cur)=> sum+cur )

    return result;
}