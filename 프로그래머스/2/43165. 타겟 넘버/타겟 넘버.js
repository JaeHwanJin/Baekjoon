function solution(number, target){
    var answer = 0;
    function dfs(index, sum){
        if(index==number.length){
            if(sum==target){
                answer += 1;
            }
            return 
        }
        dfs(index+1, sum + number[index])
        dfs(index+1, sum - number[index])
    }
    dfs(0, 0)
    return answer
}