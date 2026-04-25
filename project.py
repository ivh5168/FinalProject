import random, time

class Player:
    def __init__(self, id):
        self.id = id
        self.pos = (9, 0) # Row, column

    def update_position(self, roll):
        row_pos = self.pos[0]
        col_pos = self.pos[1]
        
        col_pos += roll

        # Send player positon to upper row
        if col_pos > 9:
            row_pos -= 1
            col_pos -= 10

        self.pos = (row_pos, col_pos)

class Game:
    def __init__(self, snakes = {17: 7, 54: 34, 62: 18, 64: 41, 87: 36, 92: 73, 95: 75, 98: 79}, ladders = {1: 38, 4: 14, 9: 30, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}):
        self.board = [
            [91,92,93,94,95,96,97,98,99,100],
            [81,82,83,84,85,86,87,88,89,90],
            [71,72,73,74,75,76,77,78,79,80],
            [61,62,63,64,65,66,67,68,69,70],
            [51,52,53,54,55,56,57,58,59,60],
            [41,42,43,44,45,46,47,48,49,50],
            [31,32,33,34,35,36,37,38,39,40],
            [21,22,23,24,25,26,27,28,29,30],
            [11,12,13,14,15,16,17,18,19,20],
            [1,2,3,4,5,6,7,8,9,10]
        ]
        self.snakes = snakes
        self.ladders = ladders

    def display_board(self):
        disp_board = self._format_board()
        
        for row in disp_board:
            print(row)

    def _format_board(self):
        disp_board = []
        for i in range(len(self.board)):
            row = self.board[i]
            if i % 2 == 0: # Even row
                row = list(reversed(row))
                disp_board.append(row)
            else: # Odd row 
                disp_board.append(row)

        return disp_board

    def roll_dice(self):
        result = random.randint(1, 6)

        return result

    def update_board(self):
        pass

    def clear_screen(self):
        print("\033[H\033[J", end="")  # ANSI escape sequence for clearing screen

    def run_game(self):
        player_input = input("\nPlayer one name: ")
        player_one = Player(player_input)
        player_input = input("\nPlayer two name: ")
        player_two = Player(player_input)
        
        self.clear_screen()
        count = 1

        while player_input.lower() != "quit" and player_input.lower() != "exit":
            self.clear_screen()
            self.display_board()
            player_input = input("\nRoll dice?")

            if player_input.lower() != "quit" and player_input.lower() != "exit":
                roll = self.roll_dice()
                
                if count % 2 == 0:
                    turn = 2
                    player_two.update_position(roll)
                else:
                    turn = 1
                    player_one.update_position(roll)

                count += 1
                
                time.sleep(1)

                print(f"Player {turn} rolled a {roll}\n")

                time.sleep(3)

def play():
    new_game = Game()
    player_input = input("Welcome to Snakes and Ladders!\nInput anything (but 'Quit' or 'Exit') to continue: \n")
    if player_input.lower() != "quit" and player_input.lower() != "exit":
        new_game.run_game()

play()