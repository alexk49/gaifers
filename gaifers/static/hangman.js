function updateCurrentWord (currentState) {
  const current = document.getElementById('current')
  current.textContent = currentState
}

function updateHangingMan (boardState) {
  const board = document.getElementById('hanging-man')

  if (boardState === 0) {
    board.textContent = ''
  }
}

function getLocalGameData (currentState, word_guess) {
  const gameData = {}

  gameData.current_word_state = currentState
  gameData.word_guess = word_guess

  return gameData
}

function resetInputText () {
  document.querySelector('#input-field').value = ''
}

async function runHangman () {
  const running = true

  // gets default new gameData
  let gd = await resetGameData('/hangman/reset')
  updateCurrentWord(gd.gameData.current_word_state)
  // reset hangman state
  updateHangingMan(gd.gameData.boardState)

  // Update guess input
  resetInputText()

  if (running) {
    submit = document.querySelector('#submit-button')

    submit.addEventListener('click', async () => {
      input = document.querySelector('#input-field').value
      if (input != '') {
        const gameDataLocal = getLocalGameData(gd.gameData.current_word_state, input)

        gd = await postGameValues(gameDataLocal, '/hangman/game')

        updateCurrentWord(gd.gameData.current_word_state)

        updateHangingMan(gd.gameData.boardState)

        resetInputText()
      }
    })
  }
}
// global script

const playHangmanButton = document.querySelector('#start-hangman')

playHangmanButton.addEventListener('click', () => {
  runHangman()
})
