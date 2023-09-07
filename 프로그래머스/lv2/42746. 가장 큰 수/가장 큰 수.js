function solution(numbers) {
  const answer = numbers
    .map((num) => num.toString()) 
    .sort((a, b) => (b + a) - (a + b))
    .join(''); 

  if (answer[0] === '0') {
    return '0';
  }

  return answer;
}

