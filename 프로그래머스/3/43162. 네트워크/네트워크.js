function solution(n, computers){
    var answer = 0;
    var visited = [false]
    function dfs(start){
        visited[start] = true;
        for(let i=0; i<computers[start].length; i++){
            if(computers[start][i] == true && visited[i] != true){
                dfs(i)    
            }
        }
    }
    
    for(let j=0; j<computers.length; j++){
        if(visited[j] != true){
            dfs(j);
            answer += 1;
        }
    }
    return answer
}