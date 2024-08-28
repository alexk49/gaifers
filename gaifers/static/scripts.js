const squares = document.querySelectorAll('.square')

squares.forEach(square => {
  square.addEventListener('mouseover', (event) => {
    square.classList.toggle('highlight-square')
  })
  square.addEventListener('mouseout', () => {
    square.classList.remove('highlight-square')
  })
})
