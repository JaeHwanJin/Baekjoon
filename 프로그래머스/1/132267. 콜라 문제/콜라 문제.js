function solution(a, b, n) {
    var newCoke = 0;
    while(n>=a){
        newCoke += Math.floor(n/a)*b;
        n = Math.floor(n/a)*b + n%a
    }
    return newCoke;
}