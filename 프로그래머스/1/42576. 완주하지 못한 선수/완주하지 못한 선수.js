function solution(participants, completion) {
    var answer = {};
    for(participant of participants){
        if(answer[participant] > 0){
            answer[participant] += 1;    
        }else{
            answer[participant] = 1;    
        }
    }
    for(winner of completion){
        answer[winner] -= 1;
    }
    for(loser in answer){
        if(answer[loser] > 0){
            return loser
        }
    }
}
