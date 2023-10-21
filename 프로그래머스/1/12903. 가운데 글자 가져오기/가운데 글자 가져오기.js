function solution(s) {
    var answer = '';
    answer = s.split("")
    var idx = parseInt(s.length/2)
    if (s.length % 2 == 0){
        return answer[idx-1]+answer[idx]
    }
    else{
        return answer[idx]
    }
    return 1
}