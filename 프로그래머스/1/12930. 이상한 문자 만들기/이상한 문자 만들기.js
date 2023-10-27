function solution(s) {
    s =s.split(" ")
    var arr = [];    
    for(const idx in s){
        var word = ""
        for(let i=0; i<s[idx].length; i++){
            if(i%2===0){
                word +=s[idx][i].toUpperCase();
            }
            if(i%2===1){
                word += s[idx][i].toLowerCase();
            }
        }
        arr.push(word)
    }
    return arr.join(" ");
}