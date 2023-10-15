function solution(n, computers){
    var answer = 0;
    var visited = Array(n).fill(0)
    function DFS(start){
        visited[start] = 1;
        for(let i=0; i<computers[start].length; i++){
            if(computers[start][i]==1 && visited[i]==0){
                DFS(i)
            }
        }
    }
    for(let j=0; j<computers.length; j++){
        if(visited[j]==0){
            DFS(j)       
            answer += 1;
        }
    }
    return answer 
}