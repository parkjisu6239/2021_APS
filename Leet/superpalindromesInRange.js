const reverseStr = (str) => {
  return str.split("").reverse().join("");
};

function checkIsPalindrome(num) {
  if (!Number.isInteger(Number(num))) {
    return false;
  }
  if (num.length === 1) {
    return true;
  }
  for (let i = 0; i < Number(num) / 2; i++) {
    if (num[i] !== num[num.length - i - 1]) {
      return false;
    }
  }
  return true;
}

function superpalindromesInRange(left, right) {
  let result = 0;
  let start = left;

  if (start < 10) {
    for (let i = Number(start); i < 10; i++) {
      if (i > Number(right)) {
        return result;
      }
      if (checkIsPalindrome(String(Math.sqrt(i)))) {
        result++;
      }
    }
    start = "10";
  }

  while (true) {
    const halfLen = Math.floor(start.length / 2);
    const isEven = start.length % 2 === 0;
    for (
      let i = Number(start.slice(0, halfLen));
      i <= Number("9".repeat(halfLen));
      i++
    ) {
      if (isEven) {
        const pal = String(i) + reverseStr(String(i));
        if (Number(pal) > Number(right)) {
          return result;
        }

        if (checkIsPalindrome(String(Math.sqrt(pal)))) {
          result++;
        }
      } else {
        for (let j = 0; j < 10; j++) {
          const pal = String(i) + String(j) + reverseStr(String(i));
          if (Number(pal) > Number(right)) {
            return result;
          }

          if (checkIsPalindrome(String(Math.sqrt(pal)))) {
            result++;
          }
        }
      }
    }
    start = "1" + "0".repeat(start.length);
  }
}

console.log(superpalindromesInRange("1", "2"));
// console.log(superpalindromesInRange("40000000000000000", "50000000000000000"));
