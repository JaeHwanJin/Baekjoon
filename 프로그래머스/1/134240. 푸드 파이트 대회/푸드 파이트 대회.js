function solution(food) {
    var answer = '';
    var list = [];
    var newList = [];
    for(let i=0; i<food.length; i++){
        if(food[i]/2>=1){
            const idx = i.toString();
            list.push(idx.repeat(Math.floor(food[i]/2)));
        }
    }
    list = list.join("");
    newList = [...list].reverse().join("");
    answer =list+"0"+newList;
    return answer;
}