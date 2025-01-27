const hangman = {
  0: `

    
    



  `,
  1: `
    
    



======
    `,
  2: `

      |
      |
      |
      |
=======
    `,
  3: `
______
      |
      |
      |
      |
=======
`,
  4: `
______
 o    |
      |
      |
      |
=======
`,
  5: `
______
 o    |
 |    |
      |
      |
=======
`,
  6: `
______
 o    |
/|    |
      |
      |
=======
    `,
  7: `
______
 o    |
/|\\   |
      |
      |
======
    `,
  8: `
______
 o    |
/|\\   |
/     |
      |
======
    `,
  9: `
______
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

function getLocalGameData (currentState, word_guess) {
  const gameData = {}

  gameData.current_word_state = currentState
  gameData.word_guess = word_guess

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

async function runHangman () {
  let running = true

  // gets default new gameData
  let gd = await resetGameData('/hangman/reset')
  updateCurrentWord(gd.gameData.current_word_state)
  // reset hangman state
  updateHangingMan(gd.gameData.incorrect_guess_count)

  // Update guess input
  resetInputText()

  resetResultBox()

  resetUsedLetters()

  if (running) {
    submit = document.querySelector('#submit-button')

    submit.addEventListener('click', async () => {
      input = document.querySelector('#input-field').value
      if (input != '') {
        if (input.length === 1) {
          writeUsedLetters(input)
        }

        const gameDataLocal = getLocalGameData(gd.gameData.current_word_state, input)

        gd = await postGameValues(gameDataLocal, '/hangman/game')

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
    })
  }
}

// global script

const playHangmanButton = document.querySelector('#start-hangman')

playHangmanButton.addEventListener('click', () => {
  runHangman()
})
