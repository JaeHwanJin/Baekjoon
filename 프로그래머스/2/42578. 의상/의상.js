function solution(clothes) {
    var answer = 1;
    var clothesMap = {}
    clothes.map(val=>{
        const [type, name] = val
        if(clothesMap.hasOwnProperty(name)){
            clothesMap[name] += 1;
        }else{
            clothesMap[name] = 1
        }
    })
    for(const val in clothesMap){
        answer *= clothesMap[val]+1
    }
    return answer-1;
}
