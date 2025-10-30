function solution(queue1, queue2) {
  const list = [...queue1, ...queue2];
  const total = list.reduce((acc, curr) => acc + curr, 0);

  if (total % 2 !== 0) {
    return -1;
  }

  let start = 0;
  let end = queue1.length - 1;
  let currentSum = list
    .slice(start, end + 1)
    .reduce((acc, curr) => acc + curr, 0);

  while (true) {
    if (currentSum === total / 2) {
      break;
    } else if (currentSum < total / 2) {
      end = (end + 1) % list.length;
      currentSum += list[end];
    } else {
      currentSum -= list[start];
      start++;
      if (start >= list.length) {
        return -1;
      }
    }
  }

  return start + end - queue1.length + 1;
}


// 처음에 진짜로 큐 클래스 만들어서 하다가 시간 초과
// 큐가 앞에꺼 빼서 뒤에 넣는거니까 그냥 쭉 연결된 리스트로 생각하고 투포인터로 접근
// 절대로 불가능한 조건 : 한바퀴 다 돌더라도 답이 나오지 않으면 -1, 합이 짝수가 아니면 -1
