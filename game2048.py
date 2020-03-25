import random
import pickle

class Game():
    def __init__(self):
        self.board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.turn = 0
        self.score = 0

    def new_game(self):
        self.board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.turn = 0
        print('new turn')
        self.new_turn()

    def get_random_number(self):
        odds_number = [2,2,2,2,2,2,2,2,2,4]
        random_number = random.choice(odds_number)
        return random_number

    def set_random_number(self):
        random_number = self.get_random_number()
        position = random.randint(0,15)
        while self.board[position] != 0 :
            position = random.randint(0,15)
        self.board[position] = random_number

    def __str__(self):
        return "Moves: "+str(self.turn-1)+"\nScore: "+str(self.score)+"\n\n"+str(self.board[0:4])+"\n"+str(self.board[4:8])+"\n"+str(self.board[8:12])+"\n"+str(self.board[12:16])
    
    def new_turn(self):
        self.update_turn_data()
        print(self)
    
    def update_turn_data(self):
        if self.turn == 0:
            self.set_random_number()
            self.set_random_number()    
        self.set_random_number()
        self.score = sum(self.board)
        self.turn += 1

    def move_up_algorithm(self):
        split_transposed_reversed_moved_reversed_transposed_rows_list = self.transpose_rows_list(self.reverse_row_in_rows_list(self.get_moved_right_rows(self.reverse_row_in_rows_list(self.transpose_rows_list(self.split_rows())))))
        self.try_update(split_transposed_reversed_moved_reversed_transposed_rows_list)

    def move_down_algorithm(self):
        split_transposed_moved_transposed_rows_list = self.transpose_rows_list(self.get_moved_right_rows(self.transpose_rows_list(self.split_rows())))
        self.try_update(split_transposed_moved_transposed_rows_list)

    def move_left_algorithm(self):
        split_reversed_moved_reversed_rows_list = self.reverse_row_in_rows_list(self.get_moved_right_rows(self.reverse_row_in_rows_list(self.split_rows())))
        self.try_update(split_reversed_moved_reversed_rows_list)

    def move_right_algorithm(self):
        split_moved_rows_list = self.get_moved_right_rows(self.split_rows())
        self.try_update(split_moved_rows_list)

    def transpose_rows_list(self,rows_list):
        return [list(transposed_rows_list) for transposed_rows_list in zip(*rows_list)]

    def reverse_row_in_rows_list(self,rows_list):
        return [list(reversed(rows_list[0])),list(reversed(rows_list[1])),list(reversed(rows_list[2])),list(reversed(rows_list[3]))]
    
    def get_moved_right_rows(self,rows_list):
        moved_rows_list = []
        for row in rows_list:
            moved_rows_list.append(self.sort_row_right(row))
        return moved_rows_list
    
    def split_rows(self):
        return [self.board[0:4],self.board[4:8],self.board[8:12],self.board[12:16]]

    def sort_row_right(self, row):
        row = self.move_row_right(row)
        row = self.join_pairs_right(row)
        row = self.move_row_right(row)
        return row

    def move_row_right(self, row):
        updated_row = []
        for value in row:
            if value == 0:
                updated_row.insert(0,0)
            else:
                updated_row.append(value)
        return updated_row
    
    def join_pairs_right(self,row):
        index = 3
        while index != 0 :
            if row[index] == row[index-1]:
                row[index] += row[index]
                row[index-1] = 0
            index -= 1
        return row
    
    def try_update(self,moved_rows_list):
        if self.rows_changed(moved_rows_list,self.split_rows()):
            self.board[0:4] = moved_rows_list[0]
            self.board[4:8] = moved_rows_list[1]
            self.board[8:12] = moved_rows_list[2]
            self.board[12:16] = moved_rows_list[3]
            self.new_turn()

    def rows_changed(self,row_list_1,row_list_2):
        return not(row_list_1 == row_list_2)

    def save_game(self):
        saved_game = open('saved_games_2048', 'wb')
        pickle.dump(self, saved_game)
        saved_game.close()

    def resume_game(self):
        saved_game = open('saved_games_2048', 'rb')
        game = pickle.load(saved_game)
        saved_game.close()
        self.board = game.board
        self.turn = game.turn
        self.score = game.score