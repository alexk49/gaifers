async function postGameValues (gameData, url) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ gameData })
  })
  const result = await response.json()

  return result
}

async function resetGameData (url) {
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  const gameData = await response.json()
  return gameData
}
