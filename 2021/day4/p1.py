# try using each number in the bingo board as the key. this would give instant look up 

from collections import OrderedDict

class BingoBoard:
    def __init__(self, board_data, rows, columns):
        self._board_data = board_data
        self._last_num_cheked = None
        self._rows = rows
        self._columns = columns
        self._bingo_row_tracker = {}
        self._bingo_column_tracker = {}

        self._marked_numbers = []
        self._unmarked_sum = None

        for i in range(rows):
            self._bingo_row_tracker[i] = []
            self._bingo_column_tracker[i] = []
        pass
    
    def check_for_number(self, num):
        if num in self._board_data:
            self._last_num_cheked = num
            row = self._board_data[num]['row']
            column = self._board_data[num]['column']

            self._bingo_row_tracker[row].append(num)
            self._bingo_column_tracker[column].append(num)

            self._board_data[num]['marked'] = True
        
    def won_game(self):
        for key, val in self._bingo_row_tracker.items():
            if len(val) == self._rows:
                return True
        for key,val in self._bingo_column_tracker.items():
            if len(val) == self._columns:
                return True
        return False

    def calculate_score(self):
        self._unmarked_sum = [key if val['marked'] == False else 0 for key, val in self._board_data.items()]
        self._unmarked_sum = sum(self._unmarked_sum)
        return self._unmarked_sum * self._last_num_cheked
        

def get_bingo_numbers_and_board():
    with open('./input') as f:
        lines = f.readlines()
    winning_numbers = [int(num) for num in lines.pop(0).split(",")]
    boards_list = []
    rows = 0
    columns = None
    board_data = OrderedDict()

    for i in range(len(lines)):
        new_board = False
        if lines[i] == '\n':
            new_board = True
            if board_data:
                bingo_board = BingoBoard(board_data=board_data, rows=rows, columns=columns)
                boards_list.append(bingo_board)
            board_data = {}
            rows = 0
        else:
            new_board = False
            board_row_lst = lines[i].rstrip().split()
            columns = len(board_row_lst)

            for i, num in enumerate(board_row_lst):
                num = int(num)
                board_data[num] = {
                    'row': rows,
                    'column': i,
                    'marked': False
                }
            rows += 1

    bingo_board = BingoBoard(board_data=board_data, rows=rows, columns=columns)
    boards_list.append(bingo_board)
    return (winning_numbers, boards_list)

def get_winning_bingo_score():
    winning_numbers, bingo_boards = get_bingo_numbers_and_board()
    found_winner = False

    for num in winning_numbers:
        for bingo_board in bingo_boards:
            bingo_board.check_for_number(num)
            if bingo_board.won_game():
                score = bingo_board.calculate_score()
                found_winner = True
                break
        if found_winner:
            break
    return score

if __name__ == '__main__':
    winning_score =  get_winning_bingo_score()
