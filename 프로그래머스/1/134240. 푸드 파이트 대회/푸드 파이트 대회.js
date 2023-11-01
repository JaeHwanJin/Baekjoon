function solution(food) {
    var answer = '';
    var list = "";
    for(let i=1; i<food.length; i++){
        list += (i.toString().repeat(Math.floor(food[i]/2)));
    }
    answer = list + "0" + [...list].reverse().join("");
    return answer;
}