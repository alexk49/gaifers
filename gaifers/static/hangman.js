import resetGameData from './scripts.js'

async function runHangman () {
  const running = true

  // gets default new gameData
  const gameData = await resetGameData('/hangman/reset')

  console.log(gameData)
}
// global script

const playHangmanButton = document.querySelector('#start-hangman')
playHangmanButton.addEventListener('click', () => {
  runHangman()
})
