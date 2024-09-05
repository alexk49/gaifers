async function updateBoardValue (boardData, square, marker) {
  const response = await fetch('/noughts/game', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ boardData })
  })
  const result = await response.json()

  if (result !== null) {
    square.textContent = marker
  } else {
    return null
  }
}

function getBoardData (squares) {
  const boardData = {}

  // gameData.new_position = square.id
  // gameData.turn = square.textContent

  // Loop through each element
  squares.forEach(square => {
    boardData[square.id] = square.textContent.trim()
  })
  return boardData
};

function assignMarkers (otherPlayer = '') {
  if (otherPlayer === 'x') {
    return 'o'
  }
  if (otherPlayer === 'o') {
    return 'x'
  }

  const validOptions = ['o', 'x']

  let playerMarker = ''

  while (validOptions.includes(playerMarker) === false) {
    playerMarker = prompt('Would player like to be x or o?')
  }
  return playerMarker
}

function updateTurn (turn, player1Marker, player2Marker) {
  // used to update turn variable to other player marker
  if (turn === player1Marker) {
    return player2Marker
  } else if (turn === player2Marker) {
    return player1Marker
  }
}

// main script

const player1Marker = assignMarkers()
const player2Marker = assignMarkers(otherPlayer = player1Marker)
let turn = player1Marker

const squares = document.querySelectorAll('.square')

squares.forEach(square => {
  square.addEventListener('mouseover', () => {
    square.classList.toggle('highlight-square')
  })
  square.addEventListener('mouseout', () => {
    square.classList.remove('highlight-square')
  })

  square.addEventListener('click', () => {
    const boardData = getBoardData(squares)
    const res = updateBoardValue(boardData, square, turn)

    if (res !== null) {
      turn = updateTurn(turn, player1Marker, player2Marker)
    }
  })
})
