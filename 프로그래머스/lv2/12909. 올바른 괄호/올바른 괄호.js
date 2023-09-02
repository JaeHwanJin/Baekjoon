function solution(s){
    var stack = [];
    if (s[0]==')'){
        return false;
    }
    for (let i=0; i<s.length; i++){
        if (s[i] == '('){
            stack.push(s[i])    
        }
        if (s[i] == ')'){
            stack.pop()
        }
    }
    if (stack.length ==0){
        return true;
    }
    if (stack.length !=0){
        return false;
    }
    
}