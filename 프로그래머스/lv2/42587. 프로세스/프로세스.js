function solution(priorities, location) {
    var cnt = 0;
    var target = location;

    while (priorities.length > 0) {
        var current = priorities.shift();
        var isPrinted = true;

        for (var i = 0; i < priorities.length; i++) {
            if (priorities[i] > current) {
                isPrinted = false;
                break;
            }
        }

        if (!isPrinted) {
            priorities.push(current);
            if (target === 0) {
                target = priorities.length - 1;
            } else {
                target--;
            }
        } else {
            cnt++;
            if (target === 0) {
                return cnt;
            } else {
                target--;
            }
        }
    }

    return cnt;
}
