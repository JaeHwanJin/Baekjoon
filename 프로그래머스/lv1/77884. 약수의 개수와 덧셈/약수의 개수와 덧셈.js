function solution(left, right) {
    var answer = 0;
    for (let i=left; i<=right; i++){
        var total = 0;
        for(let j=1; j**2<=i; j++){
            if(j**2==i){
                total+=1
            }
            if(i%j==0){
                total+=2
            }
        }
        if(total%2==0){
            answer+=i
        }
        if(total%2!=0){
            answer-=i
        }
    }
    
    return answer;
}