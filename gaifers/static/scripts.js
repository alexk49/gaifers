async function postGameValues (gameData) {
  const response = await fetch('/noughts/game', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ gameData })
  })
  const result = await response.json()

  return result
}

function getLocalGameData (squares, square, turnMarker) {
  const gameData = {}

  gameData.new_position = square.id
  gameData.playerMarker = turnMarker

  gameData.boardData = {}

  // Loop through each element
  squares.forEach(square => {
    gameData.boardData[square.id] = square.textContent.trim()
  })
  return gameData
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

function updateTurnMarker (turnMarker, player1Marker, player2Marker) {
  // used to update turn variable to other player marker
  if (turnMarker === player1Marker) {
    return player2Marker
  } else if (turnMarker === player2Marker) {
    return player1Marker
  }
}

function updateBoard (boardData, squares) {
  // used to fully update board with
  // all values passed from gameData
  squares.forEach(square => {
    if (boardData[square.id] !== undefined) {
      square.innerText = boardData[square.id]
    }
  })
}

async function resetGameData () {
  const response = await fetch('/noughts/reset', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  const gameData = await response.json()
  return gameData
}

function writeWinner (resultBox, marker) {
  resultBox.textContent = marker + ' is the winner!'
}

function writeDraw (resultBox) {
  resultBox.textContent = "It's a draw!"
}

async function runGame () {
  let running = true

  let turnMarker = ''

  // gets default new gameData
  let gameData = await resetGameData()

  const resultBox = document.querySelector('.result')
  const squares = document.querySelectorAll('.square')
  // reset board with default gameData
  updateBoard(gameData.gameData.boardData, squares)
  resultBox.textContent = ''

  const player1Marker = assignMarkers()
  // const player2Marker = assignMarkers(otherPlayer = player1Marker)
  turnMarker = player1Marker

  squares.forEach(square => {
    square.addEventListener('mouseover', () => {
      square.classList.toggle('highlight-square')
    })
    square.addEventListener('mouseout', () => {
      square.classList.remove('highlight-square')
    })

    // has to be async to await results of
    // async postGameValues
    square.addEventListener('click', async () => {
      if (square.textContent === '') {
        const gameDataLocal = getLocalGameData(squares, square, turnMarker)

        if (running) {
          gameData = await postGameValues(gameDataLocal, square, turnMarker)

          if (gameData.gameData.winner) {
            updateBoard(gameData.gameData.boardData, squares)
            writeWinner(resultBox, turnMarker)
            running = false
          } else if (gameData.gameData.draw) {
            updateBoard(gameData.gameData.boardData, squares)
            writeDraw(resultBox, turnMarker)
            running = false
          } else {
            updateBoard(gameData.gameData.boardData, squares)
            // turnMarker = updateTurnMarker(turnMarker, player1Marker, player2Marker)
            turnMarker = gameData.gameData.playerMarker
          }
        }
      }
    })
  })
}

// global script

const playButton = document.querySelector('#start-noughts')
playButton.addEventListener('click', () => {
  runGame()
})
