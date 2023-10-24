function solution(n, m) {
    function gcd(a, b) {
  const remainder = a % b;  // 1번
  if (remainder === 0) return b;  // 2번
  return gcd(b, remainder);  // 3번
}
    const gcdNum = gcd(n, m);
    const lcmNum = (n*m)/gcdNum;
    var answer = [gcdNum, lcmNum];
    return answer;
}