function solution(s, skip, index) {
    var answer = "";
    var alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'].filter((alphabet)=>!skip.includes(alphabet))
    for(s of s){
        const idx = (alphabets.indexOf(s) + index) % alphabets.length;
        answer+=alphabets[idx]
    }
    return answer;
}