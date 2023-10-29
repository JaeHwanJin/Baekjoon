function solution(s, n) {
    var answer='';
    var upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lower="abcdefghijklmnopqrstuvwxyz"
    for(let i=0; i<s.length; i++){
        if(s[i]===" "){
            answer += " "
        }
        if(upper.includes(s[i])){
            var upperNum = upper.indexOf(s[i])+n;
            if(upperNum>=upper.length){
               upperNum -= 26 ;
            }
            answer += upper[upperNum];
        }
        if(lower.includes(s[i])){
            var lowerNum = lower.indexOf(s[i])+n;
            if(lowerNum>=lower.length){
               lowerNum -= 26 
            }
            answer += lower[lowerNum];
        }
    }
    return answer;
}