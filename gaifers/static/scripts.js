async function updateGameValue (gameData, square, turnMarker) {
  const response = await fetch('/noughts/game', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ gameData })
  })
  const result = await response.json()

  if (result !== null) {
    square.textContent = turnMarker
  } else {
    return null
  }
}

function getGameData (squares, square, turnMarker) {
  const gameData = {}

  gameData.new_position = square.id
  gameData.playerMarker = turnMarker

  gameData.boardData = {}

  // Loop through each element
  squares.forEach(square => {
    gameData.boardData[square.id] = square.textContent.trim()
  })
  console.log(gameData)
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

function runGame () {
  const player1Marker = assignMarkers()
  const player2Marker = assignMarkers(otherPlayer = player1Marker)
  let turnMarker = player1Marker

  const squares = document.querySelectorAll('.square')

  squares.forEach(square => {
    square.addEventListener('mouseover', () => {
      square.classList.toggle('highlight-square')
    })
    square.addEventListener('mouseout', () => {
      square.classList.remove('highlight-square')
    })

    square.addEventListener('click', () => {
      const gameData = getGameData(squares, square, turnMarker)
      const res = updateGameValue(gameData, square, turnMarker)

      if (res !== null) {
        turnMarker = updateTurnMarker(turnMarker, player1Marker, player2Marker)
      }
    })
  })
}

// main script

playButton = document.querySelector('#start-noughts')
playButton.addEventListener('click', () => {
  runGame()
})
