function solution(prices) {
    var answer = [];
    for(let i=0; i<prices.length; i++){
        let time = 0;
        for(let j=i+1; j<prices.length; j++){
            if(prices[i]<=prices[j]){
                time+=1;
            }
            else if(prices[i]-prices[j] === 1){
                time+=1;
                break;
            }
            else{
                time+=1;
                break;
            }
        }
        answer.push(time)
    }
    return answer;
}