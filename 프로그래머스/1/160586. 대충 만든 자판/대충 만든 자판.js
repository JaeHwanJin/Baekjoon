function solution(keymap, targets) {
    var answer = [];
    var map = new Map();
    for(key of keymap){
        for(let i=0; i<key.length; i++){
            if(map.has(key[i])){
                if(map.get(key[i])>i+1){
                    map.set(key[i], i+1)
                }
            }else{
                map.set(key[i],i+1)
            }
        }
    }
    for(target of targets){
        var cnt = 0;
        for(let j=0; j<target.length; j++){
            cnt += map.get(target[j])
        }
        answer.push(cnt || -1)
    }
    return answer;
}
