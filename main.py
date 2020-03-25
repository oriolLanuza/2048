from game2048 import Game
import pickle

def main():
    print("Welcome to 2048! Are you ready to play?")
    execute_command(get_command())

def get_command():
    command = input("\t 1. New Game \n \t 2. Resume Game \n \t 3. Exit Game \n \t --->")
    if check_command(command):
        return command
    else:
        print("Oops, I didn't understand you. Can you select your option again?")
        get_command()

def check_command(command):
    return command in ["1","2","3"]

def execute_command(command):
    if command == "1":
        new_game()
    elif command == "2":
        resume_game()
    else:
        exit_game()

def new_game():
    print("You created a new game!")
    game = Game()
    game.new_game()
    game_loop(game)

def game_loop(game):
    execute_move(get_move(),game)

def get_move():
    return str(input('Enter new move (use -> w a s d): '))

def execute_move(move,game):
    if move == 'w':
        game.move_up_algorithm()
    elif move == 'a':
        game.move_left_algorithm()
    elif move == 's':
        game.move_down_algorithm()
    elif move == 'd':
        game.move_right_algorithm()
    else:
        game.save_game()
        print('Please, enter a correct move.')
    game_loop(game)

def resume_game():
    saved_game = open('saved_games_2048', 'rb')
    game = pickle.load(saved_game)
    saved_game.close()
    print(game)
    game_loop(game)
    print("You resumed last game!")

def exit_game():
    print("See you soon!")

main()