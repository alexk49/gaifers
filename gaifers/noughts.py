"""A game of noughts and crosses"""

game_data_default = {
    "gameData": {
        "new_position": "",
        "playerMarker": "",
        "winner": "false",
        "draw": "false",
        "boardData": {
            "top-left": "",
            "top-center": "",
            "top-right": "",
            "middle-left": "",
            "center": "",
            "middle-right": "",
            "bottom-left": "",
            "bottom-center": "",
            "bottom-right": "",
        },
    }
}


def check_for_draw(game_data: dict) -> bool:
    """Check game data for draw,
    runs after check for win, if any blank values remain
    then not yet draw"""
    for value in game_data_default["gameData"]["boardData"].values():
        if value == "":
            return False
    return True


def check_for_winner(game_data: dict) -> bool:
    """Check game data for a winner"""
    board = game_data["gameData"]["boardData"]
    marker = game_data["gameData"]["playerMarker"]

    print(board)
    print(marker)

    if (
        (board["top-left"] == board["top-center"] == board["top-right"] == marker)
        or (board["middle-left"] == board["center"] == board["middle-right"] == marker)
        or (board["bottom-left"] == board["bottom-center"] == board["bottom-right"] == marker)
    ):
        return True
    elif (
        (board["top-left"] == board["middle-left"] == board["bottom-left"] == marker)
        or (board["top-center"] == board["center"] == board["bottom-center"] == marker)
        or (board["top-right"] == board["middle-right"] == board["bottom-right"] == marker)
    ):
        return True
    elif (board["top-left"] == board["center"] == board["bottom-right"] == marker) or (
        board["top-right"] == board["center"] == board["bottom-left"] == marker
    ):
        return True
    else:
        return False


def validate_game_data(game_data: dict, org_game_data: dict) -> bool:
    """Check game data for any changes
    Dicts should be the same values until the new position is updated
    """
    new_position = game_data["gameData"]["new_position"]

    for key in game_data["gameData"]["boardData"]:
        if key == new_position and game_data["gameData"]["boardData"][key] != "":
            print(f"{new_position} is not empty square")
            return False
        elif game_data["gameData"]["boardData"][key] != org_game_data["gameData"]["boardData"][key]:
            print("new gameData doesn't match old gameData")
            return False
    return True


class Player:
    """Player class for noughts and crosses
    Optional arg if other player already assigned"""

    def __init__(self, other_player=""):

        self.marker = self.play_as(other_player)

    @classmethod
    def play_as(cls, other_player) -> str:
        """If other_player is given then assigns opposite marker,
        otherwise, prompts player to choose x or o"""

        if other_player == "x":
            return "o"
        if other_player == "o":
            return "x"

        valid_options = ["o", "x"]

        choice = ""

        while choice not in valid_options:

            choice = input("Would you like to play as noughts or crosses: o or x? ").lower()

        if choice == "o":
            return "o"
        else:
            return "x"

    def choose_position(self) -> int:
        """Prompt user to choose position on board
        Validates that player picks a digit in range 1 to 9"""

        valid = False

        while valid is False:
            player_choice = input(f"Where would {self.marker} like to go 123456789? ")

            try:
                position = int(player_choice)
                if (position < 1) or (position > 9):
                    raise ValueError
                valid = True
            except ValueError:
                print("You have to choose a number, between 1 and 9")
        return position


class GameBoard:
    """Noughts and Crosses Gameboard"""

    def __init__(self):
        """Sets defaults for new game on __init__"""
        self.board = self.new_board()
        self.winner = False
        self.playing = False

    def new_board(self) -> list:
        """creates empty board state"""
        return [" "] * 9

    def display_board(self):
        """updates board and prints out to terminal as noughts and crosses board"""
        print(
            f"""
            {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}
            -------------
            {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}
            -------------
            {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}
            """
        )

    def update_board(self, position: int, player_marker: str):
        """Player chooses number between 1 and 9 to represent position on board.

        For example, 1 equals top left hand corner of board, and 5 equals center.
        The self.board list counts from 0 to 8, so 1 is removed when updating index
        """
        self.board[position - 1] = player_marker

    def validate_position(self, position: int) -> bool:
        """Checks if given position is available on the board"""

        if self.board[position - 1] != " ":
            print("You must pick an empty space on the board")
            return False
        return True

    def check_for_winner(self, player_marker: str) -> bool:
        """Checks for any possible winning condition

        returns self.winner as bool so can be used as a test condition:
        self.check_for_winner(self, player_marker):
        """

        # check for horizontal win
        # [0, 1, 2] or [3, 4, 5] or [6, 7, 8]
        if (
            (self.board[0] == self.board[1] == self.board[2] == player_marker)
            or (self.board[3] == self.board[4] == self.board[5] == player_marker)
            or (self.board[6] == self.board[7] == self.board[8] == player_marker)
        ):
            self.winner = True
        # check for vertical win
        # [0, 3, 6] or [1, 4, 7], or [2, 5, 8]
        elif (
            (self.board[0] == self.board[3] == self.board[6] == player_marker)
            or (self.board[1] == self.board[4] == self.board[7] == player_marker)
            or (self.board[2] == self.board[5] == self.board[8] == player_marker)
        ):
            self.winner = True
        # check for diagonal win
        # [0, 4, 8] or [2, 4, 6]
        elif (self.board[0] == self.board[4] == self.board[8] == player_marker) or (
            self.board[2] == self.board[4] == self.board[6] == player_marker
        ):
            self.winner = True
        return self.winner

    def check_for_draw(self) -> bool:
        """Checks board for blank tile, if a single tile is blank
        then not all moves have been played and it is not a draw.

        This is only called after self.check_for_winner(), meaning
        that it can assume self.winner is False.
        """
        for tile in self.board:
            if tile == " ":
                return False
        self.declare_draw()
        return True

    def declare_draw(self):
        """Players tie: board is shown for last time,
        and then game is reset"""
        print("\nIt's a draw!\n")
        self.end_game()

    def declare_winner(self, player_marker: str):
        """Winning player marker is passed and printed out
        Board is shown for last time and then game is reset"""
        print(f"\n{player_marker} wins!\n")
        self.end_game()

    def end_game(self):
        """Displays final board and resets self.playing"""
        print("final board: \n")
        self.display_board()
        self.playing = False
        # if a draw then everyone is a winner:
        self.winner = True

    def play_game(self):
        """Runs a whole game of noughts and crosses,
        will keep looping if player chooses to play again"""

        self.board = self.new_board()

        self.playing = True
        self.winner = False

        player1 = Player()
        player2 = Player(other_player=player1.marker)

        while self.playing:
            if not self.winner:
                self.take_turn(player1)

            if not self.winner:
                self.take_turn(player2)

        self.play_again()

    def take_turn(self, player: Player):
        """Player takes their turn in game"""
        self.display_board()

        position = player.choose_position()
        while not self.validate_position(position):
            position = player.choose_position()

        self.update_board(position, player.marker)

        if self.check_for_winner(player.marker):
            self.declare_winner(player.marker)

        self.check_for_draw()

    def play_again(self):
        again = input("would you like to play again? y/n ").lower()

        if again == "y":
            self.play_game()


def main():
    gameboard = GameBoard()
    gameboard.play_game()


if __name__ == "__main__":
    main()
