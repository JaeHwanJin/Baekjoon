function solution(s) {
    let stack = [];
    let ans = [];
    
    for(let i=0; i<s.length; i++){
        if(!stack.includes(s[i])){
            stack.push(s[i])
            ans.push(-1)
            continue;
        }
        if(stack.includes(s[i])){
            ans.push(Math.abs(stack.lastIndexOf(s[i])-i))
            stack.push(s[i])
            continue;
        }
    }
    return ans;
}