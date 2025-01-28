import { postGameValues, resetGameData } from './helpers.js'

const hangman = {
  0: `






 `,
  1: `





 =====
    `,
  2: `

      |
      |
      |
      |
 ======
    `,
  3: `
 _____
      |
      |
      |
      |
 ======
    `,
  4: `
 _____
 o    |
      |
      |
      |
 ======
    `,
  5: `
 _____
 o    |
 |    |
      |
      |
 ======
    `,
  6: `
 _____
 o    |
/|    |
      |
      |
 ======
    `,
  7: `
 _____
 o    |
/|\\   |
      |
      |
 ======
    `,
  8: `
 _____
 o    |
/|\\   |
/     |
      |
 ======
    `,
  9: `
 _____
 o    |
/|\\   |
/ \\   |
      |
======
    `
}

function writeWinner () {
  const resultBox = document.getElementById('result')
  resultBox.textContent = 'You guessed the word correctly!'
}

function writeLoser (word) {
  const resultBox = document.getElementById('result')
  resultBox.textContent = 'Oh no, you lose. The word was: ' + word
}

function resetResultBox () {
  document.getElementById('result').textContent = ''
}

function updateCurrentWord (currentState) {
  const current = document.getElementById('current')
  current.textContent = currentState
}

function updateHangingMan (count) {
  const board = document.getElementById('hanging-man')

  if (count > 9) {
    count = 9
  }

  board.textContent = hangman[count]
}

function getLocalGameData (currentState, wordGuess) {
  const gameData = {}

  gameData.current_word_state = currentState
  gameData.word_guess = wordGuess

  return gameData
}

function resetInputText () {
  document.querySelector('#input-field').value = ''
}

function writeUsedLetters (letter) {
  const letters = document.getElementById('used-letters')
  if (letters.textContent.includes(letter)) {
    return
  }
  if (letters.textContent === '') {
    letters.textContent = 'Used letters: ' + letter
  } else {
    letters.textContent = 'Used letters: ' + letters.textContent.slice(14) + ', ' + letter
  }
}

function resetUsedLetters () {
  document.getElementById('used-letters').textContent = ''
}

async function submitWord (running) {
  const input = document.querySelector('#input-field').value
  if (input !== '') {
    if (input.length === 1) {
      writeUsedLetters(input)
    }

    const currentWordState = document.getElementById('current').textContent

    const gameDataLocal = getLocalGameData(currentWordState, input)

    const gd = await postGameValues(gameDataLocal, '/hangman/game')

    console.log(gd.gameData)

    updateCurrentWord(gd.gameData.current_word_state)

    updateHangingMan(gd.gameData.incorrect_guess_count)

    resetInputText()

    if (gd.gameData.winner === true) {
      writeWinner()
      running = false
    } else if (gd.gameData.incorrect_guess_count >= 9) {
      writeLoser()
      running = false
    }
  }
  return running
}

async function runHangman () {
  let running = true

  // gets default new gameData
  const gd = await resetGameData('/hangman/reset')
  updateCurrentWord(gd.gameData.current_word_state)
  // reset hangman state
  updateHangingMan(gd.gameData.incorrect_guess_count)

  // Update guess input
  resetInputText()

  resetResultBox()

  resetUsedLetters()

  if (running) {
    const submit = document.querySelector('#submit-button')

    const handleSubmit = () => {
      running = submitWord(running)
      if (!running) {
        // If `running` is false, remove event listeners
        submit.removeEventListener('click', handleSubmit)
        document.removeEventListener('keydown', handleKeydown)
        console.log('Event listeners removed.')
      }
    }

    const handleKeydown = (event) => {
      if (event.key === 'Enter') {
        handleSubmit()
      }
    }

    submit.addEventListener('click', handleSubmit)
    document.addEventListener('keydown', handleKeydown)
  }
}

// global script

const playHangmanButton = document.getElementById('start-hangman')

playHangmanButton.addEventListener('click', () => {
  runHangman()
})
