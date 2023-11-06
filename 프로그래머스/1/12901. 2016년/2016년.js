function solution(a, b) {
    var days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    var day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    var sum = 0;
    for(let i=0; i<a; i++){
        sum+= days[i]
    }
    sum += b
    if(a<3){
        var answer = day[sum%7-1]    
    }
    else{
        var answer = day[sum%7]
    }
    return answer;
}