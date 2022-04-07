from board import board, player


class game():
    def __init__(self, num_of_games):
        self.num_of_games = num_of_games
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0

    def simulate(self, xbot, obot, print_game = False):
        for _ in range(self.num_of_games):
            board_ = board()
            current_turn = player.x
            winner = None
            for i in range(9):
                choice = []
                if(current_turn == xbot.player):
                    choice = xbot.select_move(board_)
                else:
                    choice = obot.select_move(board_)
                board_.make_move(choice[0], choice[1], current_turn)

                winner = board_.has_winner()

                if print_game:
                    board_.print()
                if (winner != None):
                    print(str(winner) + " has won.")
                    break
                elif(i == 8):
                    print("Tied.")
                    break
                current_turn = current_turn.other
            if(winner == player.x):
                self.x_wins += 1
            elif(winner == player.o):
                self.o_wins += 1
            else:
                self.ties += 1

        print("X: " + str(self.x_wins))
        print("O: " + str(self.o_wins))
        print("Tied: " + str(self.ties))
