function solution(progresses, speeds){
    var answer = []
    var newProgresses = progresses.map((progress, index, day) => ({ progress, index,day : Math.ceil((100-progress)/speeds[index])}));
    console.log(newProgresses)
    var maxDay = newProgresses[0].day
    var cnt = 0;
    for(let i=0; i<newProgresses.length; i++){
        if(newProgresses[i].day > maxDay){
            maxDay = newProgresses[i].day
            answer.push(cnt)
            cnt = 0
        }
        if(newProgresses[i].day <= maxDay){
            cnt++;
        }
    }
    answer.push(cnt)
    
    return answer;
}