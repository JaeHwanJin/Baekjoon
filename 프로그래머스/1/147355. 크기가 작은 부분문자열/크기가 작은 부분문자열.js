function solution(t, p) {
    var answer = 0;
    var lst = [];
    for(let i=0; i<t.length-p.length+1; i++){
        lst.push(t.slice(i,i+p.length));
    }
    for(let j=0; j<lst.length; j++){
        if(parseInt(lst[j])<=parseInt(p)){
            answer++;
        }
    }
    return answer;
}