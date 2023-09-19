function solution(s) {
    var answer = '';
    var words = s.split(" ");
    
    for(let i=0; i<words.length; i++){
        var word = words[i];
        if(word.length > 0){
            word = word[0].toUpperCase()+word.slice(1).toLowerCase();
        }
        words[i]=word;
    }
    answer = words.join(" ");
    return answer;
}
