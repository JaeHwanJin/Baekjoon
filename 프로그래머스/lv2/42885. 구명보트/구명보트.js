function solution(people, limit) {
    var answer = 0;
    var right = people.length - 1;
    var left = 0;
    people.sort((a,b)=> b-a)  
    while(left<= right){
        if(people[left] + people[right] <= limit){
            left++;
            right--;
        }
        else{
            left++;
        }
        answer++;
    }
    return answer;
}