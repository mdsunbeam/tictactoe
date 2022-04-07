from board import player
from game import game
from agents import RandomAgent

def main():
    xbot = RandomAgent(player.x)
    obot = RandomAgent(player.o)
    game_ = game(1000)
    game_.simulate(xbot, obot)

if __name__ == '__main__':
    main()