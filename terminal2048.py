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
    execute_option(get_move(),game)

def get_move():
    return str(input('Use w a s d to move, save or exit: '))

def execute_option(option,game):
    if option == 'w':
        game.move_up_algorithm()
    elif option == 'a':
        game.move_left_algorithm()
    elif option == 's':
        game.move_down_algorithm()
    elif option == 'd':
        game.move_right_algorithm()
    elif option == 'save':
        game.save_game()
    elif option == 'exit':
        exit_game()
        return
    else:
        print('Please, enter a correct command.')
    game_loop(game)

def resume_game():
    saved_game = open('saved_games_2048', 'rb')
    game = pickle.load(saved_game)
    saved_game.close()
    print(game)
    print("You resumed last game saved!")
    game_loop(game)

def exit_game():
    print("See you soon!")

main()