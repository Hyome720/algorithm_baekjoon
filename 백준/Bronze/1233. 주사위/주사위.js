let [a, b, c] = require('fs').readFileSync(0, 'utf-8').split(' ').map(Number);
let arr = Array(81).fill(0)

for (let i = 1; i <= a; i++) {
  for (let j = 1; j <= b; j++) {
    for (let k = 1; k <= c; k++) {
      arr[i + j + k] += 1
    }
  }
}

const maxValue = Math.max(...arr)
const resIdx = arr.indexOf(maxValue)

console.log(resIdx)