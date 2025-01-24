async function runHangman () {
  const running = true

  // gets default new gameData
  const gd = await resetGameData('/hangman/reset')
  updateCurrentWord(gd.current_word_state)
  // reset hangman state
}
// global script

const playHangmanButton = document.querySelector('#start-hangman')
playHangmanButton.addEventListener('click', () => {
  runHangman()
})

function updateCurrentWord (currentState) {
  const current = document.getElementById('current')
  current.textContent = currentState
  console.log(current)
  console.log(currentState)
}
