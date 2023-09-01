function solution(X, Y) {
    let answer = [];
    let newX = X.split("").sort((a, b) => b - a);
    let newY = Y.split("").sort((a, b) => b - a)
    
    
    const larger = newX.length > newY.length ? newX:newY
    const smaller = newX.length <= newY.length ? newX:newY
   
    let p1 = 0;
    let p2 = 0;
    console.log(larger)
    console.log(smaller)
    while(p1<smaller.length && p2<larger.length){
        if(smaller[p1]=== larger[p2]){
            answer.push(smaller[p1])
            p1++;
            p2++;
            continue;
        }
        else{
            if(smaller[p1] > larger[p2]){
                p1++;
            }
            else{
                p2++;
            }
        }
    }
    if (answer == ""){
        return "-1"
    }
    if (answer.every((num)=>num==0)){
        return "0"
    }
    return answer.join("")
}