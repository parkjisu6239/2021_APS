const reverseStr = (str) => {
  return str.split("").reverse().join("");
};

const getPal = (left, right) => {
  let result = 0;
  let start = left;
  while (true) {
    const halfLen = Math.floor(start.length / 2);
    const isEven = start.length % 2 === 0;
    for (
      let i = Number(start.slice(0, halfLen));
      i <= Number("9".repeat(halfLen));
      i++
    ) {
      if (isEven) {
        if (Number(String(i) + reverseStr(String(i))) > Number(right)) {
          return result;
        }

        result++;
        console.log(String(i) + reverseStr(String(i)));
      } else {
        for (let j = 0; j < 10; j++) {
          if (
            Number(String(i) + String(j) + reverseStr(String(i))) >
            Number(right)
          ) {
            return result;
          }

          result++;
          console.log(String(i) + String(j) + reverseStr(String(i)));
        }
      }
    }
    start = "1" + "0".repeat(start.length);
  }
};

console.log(getPal("100", "2000"));
