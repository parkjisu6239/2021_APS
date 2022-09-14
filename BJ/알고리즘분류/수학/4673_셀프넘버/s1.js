const nums = Array(10001)

function d(n) {
  let result = n;
  while (n > 0) {
    result += n % 10
    n = parseInt(n / 10)
  }
  return result
}

for(i=1; i<10001; i++) {
  let cur = i
  if (nums[cur] === 1) {
    continue
  }

  while (cur < 10001) {
    cur = d(cur)
    nums[cur] = 1
  }
}

for(i=1; i<10001; i++) {
  if (nums[i] === 0) {
    console.log(i)
  }
}