// function solution(maps) {
//     let answer = 1;
//     let visited = maps;
//     let queue = [];
//     const dx = [-1, 1, 0, 0];
//     const dy = [0, 0, -1, 1];
//     const n = maps.length;
//     const m = maps[0].length;
    
//     queue.push([0, 0]);
//     visited[0][0] = 0;
    
//     while(queue.length > 0) {
//         let size = queue.length;
        
//         for(let i = 0; i < size; i++) {
//             let [x, y] = queue.shift();
            
//             for(let j = 0; j < 4; j++) {
//                 let nx = x + dx[j];
//                 let ny = y + dy[j];
                
//                 if(nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] === 1) {
//                     if(nx == n - 1 && ny == m - 1) {
//                         return ++answer;
//                     }
//                     queue.push([nx, ny]);
//                     visited[nx][ny] = 0;
//                 }
//             }
//         }
//         answer++;
//     }
    
//     return -1;
// }

function solution(maps){
    var answer = 1;
    let visited = maps;
    let queue = [];
    queue.push([0,0])
    var mx = [0,0,1,-1];
    var my = [1,-1,0,0];
    var row = maps.length;
    var col = maps[0].length;
    

    visited[0][0] = 0;
    
    
    while(queue.length>0){
        let size = queue.length
        for(let i=0; i<size; i++){
            var [x, y] = queue.shift();
            for(let j=0; j<4; j++){
                var nx = x+mx[j];
                var ny = y+my[j];
                if(nx>=0 && ny>=0 && nx<row && ny<col && visited[nx][ny]===1){
                    if(nx===row-1 && ny===col-1){
                        return ++answer;
                    }
                    queue.push([nx,ny])
                    visited[nx][ny] = 0;
                }
            }
        }
        answer++;
    }
    return -1;
}
// function solution(maps) {
//     const mx = [0, 0, 1, -1];
//     const my = [1, -1, 0, 0];
//     const row = maps.length;
//     const col = maps[0].length;
//     const queue = [[0, 0]];
//     const visited = new Array(row).fill().map(() => new Array(col).fill(0));
//     visited[0][0] = 1;
//     let answer = 1;

//     while (queue.length > 0) {
//         const queueLength = queue.length;
//         for (let i = 0; i < queueLength; i++) {
//             const [x, y] = queue.shift();
//             for (let j = 0; j < 4; j++) {
//                 const nx = x + mx[j];
//                 const ny = y + my[j];
//                 if (nx >= 0 && ny >= 0 && nx < row && ny < col && maps[nx][ny] === 1 && visited[nx][ny] === 0) {
//                     if (nx === row - 1 && ny === col - 1) {
//                         return answer + 1;
//                     }
//                     queue.push([nx, ny]);
//                     visited[nx][ny] = 1;
//                 }
//             }
//         }
//         answer++;
//     }

//     return -1;
// }
