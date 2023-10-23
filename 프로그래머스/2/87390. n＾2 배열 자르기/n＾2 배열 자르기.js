function solution(n, left, right) {
    const answer = [];
    for(let i = left; i<right+1; i++){
        const x = Math.floor(i/n);
        const y = Math.floor(i%n);
        answer.push(Math.max(x, y) + 1);
    }
    

    return answer;
}