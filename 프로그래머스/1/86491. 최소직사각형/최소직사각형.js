function solution(sizes){
    var answer=0;
    var w = [];
    var h = [];
    for(let i=0; i<sizes.length; i++){
        w.push(Math.max(...sizes[i]))                
        h.push(Math.min(...sizes[i]))
    }
    answer = Math.max(...w)*Math.max(...h)
    return answer; 
}
