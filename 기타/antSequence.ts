type StrList = string[]

function ant(str: string) {
  const strList: StrList = str.split("")
  const result: StrList[] = []
  let temp: StrList = []
  strList.forEach((str) => {
    if (temp.length === 0) {
      temp.push(str)
    } else {
      if (temp[temp.length - 1] === str) {
        temp.push(str)
      } else {
        result.push(temp)
        temp = [str]
      }
    }
  })

  if (temp) {
    result.push(temp)
    temp = []
  }

  return result.reduce((prev, cur) => {
    return prev + cur[0] + cur.length.toString()
  }, "")
}

let value = "1"
console.log(value)
for(let i=0; i < 10; i++) {
  value = ant(value)
  console.log(value)
}
