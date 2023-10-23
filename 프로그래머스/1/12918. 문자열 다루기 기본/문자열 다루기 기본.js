function solution(s) {
    const lst = s.split("")
    
    if((s.length === 4 || s.length === 6 )&&lst.every(val=> !isNaN(val))){
        return true
    }
    return false;
}