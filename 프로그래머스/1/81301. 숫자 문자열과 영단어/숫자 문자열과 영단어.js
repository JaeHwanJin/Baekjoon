function solution(s) {
    var words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    var lst = [];
    var word = "";
    for(let i=0; i<s.length; i++){
        if(isNaN(s[i])){
            word += s[i];
        }
        if(!isNaN(s[i])){
            lst.push(s[i])
        }
        if(words.includes(word)){
            lst.push(words.indexOf(word))
            word = ""    
        }   
    }
    var answer = Number(lst.join(""));
    return answer;
}