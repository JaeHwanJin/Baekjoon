function solution(citations) {
    var count = 0;
    var answer = 0;
    var lst = citations.sort((a,b)=> b-a)
    while(lst[count]>count){
        answer ++;
        count ++;
    }
    
    return answer;
}