"""
Game of hangman

Computer picks word, number of letters get written on screen

User guesses letter at a time OR guesses word

if letter is in word then all instances of letter are revealed.

if all word is revealed or word is guessed correctly then game is won.

If letter is not in word or word is incorrect then a life is loss, there are roughly 9 lives

and a line should be drawn on screen


- - - - 
                 ____
                |   |
                o   |
               /|\  |
               / \  |
                    =
"""
from os.path import abspath
from secrets import randbelow

hangman = {
    "1": """






    =====
    """,
    "2": """


         |
         |
         |
         |
    ======
    """,
    "3": """

    _____
         |
         |
         |
         |
    ======
    """,
    "4": """

    _____
    o    |
         |
         |
         |
    ======
    """,
    "5": """

    _____
    o    |
    |    |
         |
         |
    ======
    """,
    "6": """

    _____
    o    |
   /|    |
         |
         |
    ======
    """,
    "7": """

    _____
    o    |
   /|\   |
         |
         |
    ======
    """,
    "8": """

    _____
    o    |
   /|\   |
   /     |
         |
    ======
    """,
    "9": """

    _____
    o    |
   /|\   |
   / \   |
         |
    ======
    """,
}

indentation = "     "


def pick_word():
    """
    Pick random word from valid options
    """
    words_file = abspath("gaifers/words")
    with open(words_file) as file:
        words = file.readlines()
        index = randbelow((len(words) + 1))
    print(words[index])
    return words[index]


def get_user_guess(word):
    """
    User makes guess of letter or word
    """
    valid = False

    while not valid:
        guess = input("Pick a letter or guess the word: ")

        if (len(guess) > 1) and (guess != len(word)):
            print(
                f"Your word is {len(guess)} letters long, and my word is {len(word)}, try again!"
            )

        if guess.isalpha() is False:
            print(f"Your guess {guess} isn't a letter, try again!")
        else:
            valid = True

    return guess


def check_for_win(guess, word):
    return guess == word


def check_word_for_guess(guess, word, result):
    success = False
    if result == []:
        result = list(" " * len(word))
    else:
        result = list(result)

    for index, char in enumerate(word):
        if char == guess:
            result[index] = char
            success = True
    result = "".join(result)
    return result, success


def print_word_area(word):
    print(indentation + "-" * len(word))


def print_board(result: str):
    print("")
    print(indentation + result)
    print_word_area(result)


def declare_winner(word):
    print("You guessed the word!")

    print_board(word)


def declare_failure(word):
    print("oh no, you didn't guess the word in time...")

    print("\nThe word was: ")
    print_board(word)


def play_game():
    win = False
    result = []
    count = 0

    word = pick_word()

    print("")
    print_word_area(word)
    print("")

    while win is False:

        guess = get_user_guess(word)

        win = check_for_win(guess, word)

        if win:
            declare_winner(word)
            break

        result, success = check_word_for_guess(guess, word, result=result)

        if success:

            win = check_for_win(result, word)

        else:
            count += 1

        if win:
            declare_winner(word)
            break

        print_board(result)

        if count > 0:
            print(hangman[str(count)])

        if count >= 9:
            declare_failure(word)
            break


def main():

    play_game()


if __name__ == "__main__":
    main()
