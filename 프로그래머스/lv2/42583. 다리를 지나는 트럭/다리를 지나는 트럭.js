function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = [];
    let bridge_weight = 0;
    while (truck_weights.length > 0) {
        answer++;
        if(bridge_length == bridge.length) {
            
            bridge_weight -= bridge.shift();
        }
        if(bridge_weight + truck_weights[0] > weight){
            bridge.push(0)
            continue;
        }
        let move_truck = truck_weights.shift();
        bridge_weight += move_truck;
        bridge.push(move_truck)
    }
    answer += bridge_length;
    return answer;
}
