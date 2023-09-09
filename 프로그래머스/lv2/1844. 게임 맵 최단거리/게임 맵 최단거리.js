function solution(maps) {
    const n = maps.length; // 맵의 행 수
    const m = maps[0].length; // 맵의 열 수
    const dx = [1, -1, 0, 0]; // 상하좌우 방향 이동을 위한 배열
    const dy = [0, 0, 1, -1]; // 상하좌우 방향 이동을 위한 배열

    const queue = []; // BFS를 위한 큐
    queue.push([0, 0, 1]); // 시작 위치와 이동 거리(1)를 큐에 추가

    while (queue.length > 0) {
        const [x, y, distance] = queue.shift(); // 큐에서 하나의 위치와 이동 거리를 가져옴

        // 상대 팀 진영에 도착한 경우, 이동 거리를 반환
        if (x === n - 1 && y === m - 1) {
            return distance;
        }

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            // 이동할 위치가 맵 범위 내에 있고, 벽이 아니라면
            if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] === 1) {
                maps[nx][ny] = 0; // 해당 위치를 방문한 것으로 표시
                queue.push([nx, ny, distance + 1]); // 다음 위치와 이동 거리를 큐에 추가
            }
        }
    }

    // 상대 팀 진영에 도착할 수 없는 경우
    return -1;
}


