function solution(n, m, k) {
  let result = 0;
  function makeLoad(width, cnt) {
    if (width <= 0 && cnt) {
      return;
    }

    if (cnt === 0) {
      if (width === 0) {
        result++;
      }
      return;
    }

    for (let i = 1; i <= k; i++) {
      makeLoad(width - i, cnt - 1);
    }
  }

  makeLoad(m, n);

  return result;
}

function getNumberOfCases(n, m, k) {
  let dp = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
  dp[0][0] = 1;

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      for (let x = 1; x <= k; x++) {
        if (j >= x) {
          dp[i][j] += dp[i - 1][j - x];
        }
      }
    }
  }

  return dp[n][m];
}

console.log(getNumberOfCases(3, 6, 3));
console.log(getNumberOfCases(3, 7, 4));
console.log(getNumberOfCases(20, 100, 50));
