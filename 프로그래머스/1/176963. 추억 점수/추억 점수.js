function solution(name, yearning, photo) {
    var answer = []
    var score = {}
    for(let i=0; i<name.length; i++){
        score[name[i]] = yearning[i]
    }
    for(let i=0; i<photo.length; i++){
        var sum = 0;
        for(let j=0; j<photo[i].length; j++){
            if(Object.keys(score).includes(photo[i][j])){
                sum+=score[photo[i][j]]
            }
        }
        answer.push(sum)
    }
    
    return answer;
}