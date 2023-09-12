function solution(n, computers) {
    var answer = 0;
    var visited = [false];
    
    function DFS(start){
        visited[start] = true
        for(let i=0; i<computers[start].length; i++){
            if(computers[start][i]==1 && !visited[i]){
                DFS(i)
            }
        }
    }
    
    for(let j=0; j<computers.length; j++){
        if(!visited[j]){
            DFS(j)
            answer+=1;
        }
        
    }
    
    return answer;
}