function solution(n, lost, reserve) {
    var realLost = lost.filter((num) => !reserve.includes(num)).sort((a, b) => a - b);
    var realReserve = reserve.filter((num) => !lost.includes(num)).sort((a, b) => a - b);
    var answer = n - realLost.length;

    for (let i = 0; i < realLost.length; i++) {
        const minus = realLost[i] - 1;
        const plus = realLost[i] + 1;

        if (realReserve.includes(minus)) {
            const idx = realReserve.indexOf(minus);
            realReserve.splice(idx, 1);
            answer++;
            continue;
        }
        
        if (realReserve.includes(plus)) {
            const idx = realReserve.indexOf(plus);
            realReserve.splice(idx, 1);
            answer++;
        }
    }
    return answer;
}
