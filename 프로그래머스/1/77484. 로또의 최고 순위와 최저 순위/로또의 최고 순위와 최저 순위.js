function solution(lottos, win_nums) {
    var answer = [];
    var correct = 0;
    var zero = 0;
    for(lotto of lottos){
        if(win_nums.includes(lotto)){
            correct += 1;
        }
        if(lotto === 0){
            zero += 1;
        }
    }
    const best = (correct + zero) === 0 ? 6 : 7 - (correct + zero);
    const worst = zero == 6 ? 6 : best + zero
    
    return [best, worst];
}