function solution(n){
    var ans = 1;
    var cnt = 1; // 이동횟수
    if(n==1){
        return 1
    }
    while(n !== 2){
        if(n%2==1){
            n-=1
            cnt++
        }else{
            n/=2
        }
    }
    return cnt;
}