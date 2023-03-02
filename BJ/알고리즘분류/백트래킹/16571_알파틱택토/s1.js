const fs = require("fs");
const input = fs.readFileSync(__dirname + "/dev/stdin.txt").toString().split('\n');

const arr = input.map(line => line.split(" ").map(ele => +ele))

function getGameInfo(arr) {
  let x = 0
  let o = 0
  arr.forEach(element => {
    element.forEach(ele => {
      if (ele === 1) {
        x++
      } else if (ele === 2) {
        o++
      }
    })
  });
  return { player: o < x ? 2 : 1, turn: 9 - x - o}
}

function deepCopy(arr) {
  let copy_arr = []
  arr.forEach(ele => {
    copy_arr.push([...ele])
  })
  return copy_arr
}

function round(board, player) {
  const copy_board = deepCopy(board) // COP
  for(let i=0; i<3; i++) {
    for(let j=0; j<3; j++) {
      if (copy_board[i][j] === 0) {
        copy_board[i][j] = player
        return copy_board
      }
    }
  }
  return copy_board
}

function getGameResult(board, player) {
  for (let i=0; i<3; i++){
    let row = 1
    let col = 1
    for(let j=0; j<3; j++) {
      row *= [board[i][j]]
      col *= [board[j][i]]
    }

    if (row === 1 || col === 1) {
      return player === 1 ? "W" : "L"
    } else if (row === 8 || col === 8) {
      return player === 2 ? "W" : "L"
    } 
  }

  let leftCross = 1
  let rightCross = 1
  for (let i=0; i<3; i++){
    leftCross *= board[i][i]
    rightCross *= board[i][2-i]
  }

  if (leftCross === 1 || rightCross === 1) {
    return player === 1 ? "W" : "L"
  } else if (leftCross === 8 || rightCross === 8) {
    return player === 2 ? "W" : "L"
  }

  return "S" // still play
}

function play(arr, curTurn, turnLimit){
  if (curTurn > turnLimit) {
    return "D"
  }
  
  const newBoard = round(arr, player)
  const result = getGameResult(newBoard, player)
  if (result !== "S") {
    return result
  } else{
    return play(newBoard, curTurn + 1, turnLimit)
  }
}

let board = deepCopy(arr)
const {player, turn} = getGameInfo(arr)
console.log(play(board, 1, turn))

