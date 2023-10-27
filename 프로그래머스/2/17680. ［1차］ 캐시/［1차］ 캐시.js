function solution(cacheSize, cities) {
    var answer = 0;
    var map = [];
    
    if (cacheSize == 0) return cities.length * 5;
    
    cities = cities.map((city) => city.toUpperCase());
    
    for(city of cities){
        if(map.includes(city)){
            const idx = map.indexOf(city)
            map.splice(idx, 1)
            map.push(city)
            answer+=1;
        }else{
            if(map.length>=cacheSize){
                map.shift();
                map.push(city);
                answer += 5;
            }
            else{
                map.push(city);
                answer += 5;
            }
        }
    }
    return answer;
}
