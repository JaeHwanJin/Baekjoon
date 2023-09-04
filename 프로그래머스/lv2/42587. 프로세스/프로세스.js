function solution(priorities, location) {
    var answer = 0;
    var maxPriority = Math.max(...priorities);
    
    while (true) {
        var current = priorities.shift();
        
        if (current === maxPriority) {
            answer++;
            if (location === 0) return answer;
            maxPriority = Math.max(...priorities);
        } else {
            priorities.push(current);
        }
        
        location = (location - 1 + priorities.length) % priorities.length;
    }
}
