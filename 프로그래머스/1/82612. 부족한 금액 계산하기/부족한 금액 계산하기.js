function solution(price, money, count) {
    var sum = 0;
    for(let i=1; i<count+1; i++){
        sum+= price*i
    }
    if(money>=sum){
        return 0;
    }else{
        return Math.abs(money-sum);    
    }
}