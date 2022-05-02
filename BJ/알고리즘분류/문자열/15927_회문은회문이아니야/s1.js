var fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
var input = fs.readFileSync('input.txt').toString().split(' ');
var value = input[0];
// 가장 긴 부분문자열 + 팰린드롬 아님
var getLCS = function (value) {
    var lsc = Array(value.length + 1).fill(0);
    for (var i = 1; i < value.length + 1; i++) {
        for (var j = 1; j < value.length + 1; j++) {
            if (value[i - 1] === value[value.length - j]) {
                lsc[j] = Math.max(lsc[j], lsc[j - 1]);
            }
            else {
                lsc[j] = lsc[j - 1] + 1;
            }
        }
    }
    return lsc[value.length];
};
console.log(getLCS(value));
