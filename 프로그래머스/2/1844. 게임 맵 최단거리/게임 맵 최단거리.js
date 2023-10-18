function solution(maps) {
    var mx = [0, 0, 1, -1];
    var my = [1, -1, 0, 0];
    var x = maps.length;
    var y = maps[0].length;
    var q = []
    q.push([0, 0, 1])
    while (q.length){
        const [curX, curY, move] = q.shift();
        if(curX==x-1 && curY==y-1){
            return move;
        }
        for(let i=0; i<4; i++){
            const vx = mx[i] + curX;
            const vy = my[i] + curY;
            if(0 <= vx && vx < x && 0 <= vy && vy < y && maps[vx][vy]==1){
                q.push([vx, vy, move+1]);
                maps[vx][vy] = 0;
            }
        }
    }
    
    return -1;
}


