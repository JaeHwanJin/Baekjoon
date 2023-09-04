function solution(priorities, location) {
    var answer = 0;
    var newPriorities = priorities.map((priority, index) => ({priority, index}));
    console.log(newPriorities)
    while (true) {
        var current = newPriorities.shift();
        console.log(current)
        var check = newPriorities.some(newPriority => newPriority.priority > current.priority)
        if(check){
            newPriorities.push(current);
        }
        else if(!check && current.index === location){
                        answer++;

            return answer;
        }
        else{
            answer++;
        }
    }
}
