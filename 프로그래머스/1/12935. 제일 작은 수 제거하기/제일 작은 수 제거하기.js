function solution(arr) {
    if(arr.length===1){
        return [-1]
    }
    var answer = [];
    // arr.sort((a, b)=> b-a)
    // console.log(arr.indexOf(Math.min(arr)))
    arr.splice(arr.indexOf(Math.min(...arr)),1);
    // arr.splice(arr.length-1)
    

    // answer = arr.splice(indexOf(Math.min))
    return arr;
}