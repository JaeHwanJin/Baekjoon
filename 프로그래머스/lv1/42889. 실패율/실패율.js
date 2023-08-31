function solution(N, stages) {
    var answer = [];
    let members = stages.length;
    
    stages.sort();
    
    for (let i = 1; i <= N; i++) {
        let count = stages.filter(num => num === i).length;
        answer.push({ stage: i, fail: count / members });
        members -= count;
    }

    answer.sort((a, b) => {
        if (a.fail === b.fail) {
            return a.stage - b.stage; 
        }
        return b.fail - a.fail; 
    });
    
    for (let k = 0; k < N; k++) {
        console.log(answer[k].fail);
    }
    
    return answer.map(item => item.stage);
}
