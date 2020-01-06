from game2048 import Game

def main():
    welcome()
    execute_command(get_command())

def welcome():
    welcome_msg = "Welcome to 2048! Are you ready to play?"
    print(welcome_msg)

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

def resume_game():
    print("You resumed last game!")

def exit_game():
    print("See you soon!")