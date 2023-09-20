function solution(s) {
    var ss = s;
    var cnt = 0;
    var zero = 0;
    var len;
    while(ss!=="1"){
        cnt++;
        for(let i=0; i<ss.length; i++){
            if(ss[i]==="0"){
                zero+=1;
            }
        }
        ss = ss.split("0").join("");
        len = ss.length;
        ss = len.toString(2);
    }
    return [cnt, zero];
}