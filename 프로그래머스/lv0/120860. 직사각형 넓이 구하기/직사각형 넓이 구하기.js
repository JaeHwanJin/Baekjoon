function solution(dots) {
    dots.sort()
    var width = Math.abs(dots[1][1] - dots[0][1])
    var length = Math.abs(dots[0][0] - dots[2][0])
    var answer = width*length
    return answer;
}