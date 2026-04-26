import random, time

class Player:
    def __init__(self, id):
        self.id = id
        self.pos = (9, 0) # Row, column
        self.int_pos = 1

    def update_position(self, roll):
        row_pos = self.pos[0]
        col_pos = self.pos[1]
        
        if self.int_pos + roll <= 100: 
            col_pos += roll
            self.int_pos += roll

        # Send player positon to upper row
        if col_pos > 9:
            row_pos -= 1
            col_pos -= 10

        self.pos = (row_pos, col_pos)

    def hit_snake(self, new_int, new_pos):
        print(f"Player {id} hit a snake!")
        self.int_pos = new_int
        self.pos = new_pos

    def hit_ladder(self, new_int, new_pos):
        print(f"Player {id} got to a ladder!")
        self.int_pos = new_int
        self.pos = new_pos

class Game:
    def __init__(self, 
    snakes = {
    17: (7, (9, 6)),
    54: (34, (6, 3)),
    62: (18, (8, 7)),
    64: (41, (5, 0)),
    87: (36, (6, 5)),
    92: (73, (2, 2)),
    95: (75, (2, 4)),
    98: (79, (2, 8))}, 
    
    ladders = {
    2: (38, (3, 7)),
    4: (14, (8, 3)),
    9: (30, (7, 9)),
    21: (42, (5, 1)),
    28: (84, (1, 3)),
    51: (67, (3, 6)),
    72: (91, (0, 0)),
    80: (99, (0, 8))
    }
    ):
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
        player_input = input("Enter 'Quit' or 'Exit' to end program at any time.")
        player_one = Player("1")
        player_two = Player("2")
        
        self.clear_screen()
        turns = 1 # Keeps track of how many turns have passed.
        turn = 1

        while player_input.lower() != "quit" and player_input.lower() != "exit":
            # Update screen
            self.clear_screen()
            self.display_board()
            print(f"\nPlayer One: {player_one.int_pos}, {player_one.pos}\nPlayer Two: {player_two.int_pos}, {player_two.pos}")

            # Determine player turn
            if turns % 2 == 0:
                turn = 2
            else:
                turn = 1

            player_input = input(f"\nPlayer {turn} roll dice?")

            if player_input.lower() != "quit" and player_input.lower() != "exit":
                roll = self.roll_dice()
                
                if turn == 1:
                    player_one.update_position(roll)

                    if player_one.int_pos in self.snakes: # Hit a snake
                        new_int = self.snakes[player_one.int_pos][0]
                        new_pos = self.snakes[player_one.int_pos][1]
                        player_one.hit_snake(new_int, new_pos)
                    elif player_one.int_pos in self.ladders: # Hit a ladder
                        new_int = self.ladders[player_one.int_pos][0]
                        new_pos = self.ladders[player_one.int_pos][1]
                        player_one.hit_ladder(new_int, new_pos)
                else: # turn == 2
                    player_two.update_position(roll)

                    if player_two.int_pos in self.snakes: # Hit a snake
                        new_int = self.snakes[player_one.int_pos][0]
                        new_pos = self.snakes[player_one.int_pos][1]
                        player_two.hit_snake(new_int, new_pos)
                    elif player_two.int_pos in self.ladders: # Hit a ladder
                        new_int = self.ladders[player_one.int_pos][0]
                        new_pos = self.ladders[player_one.int_pos][1]
                        player_two.hit_ladder(new_int, new_pos)
                    
                turns += 1
                
                time.sleep(2)

                # Update screen
                self.clear_screen()
                self.display_board()
                print(f"\nPlayer One: {player_one.int_pos}, {player_one.pos}\nPlayer Two: {player_two.int_pos}, {player_two.pos}")
                print(f"\nPlayer {turn} rolled a {roll}")

                time.sleep(4)

def play():
    new_game = Game()
    player_input = input("Welcome to Snakes and Ladders!\nInput anything (but 'Quit' or 'Exit') to continue: \n")
    if player_input.lower() != "quit" and player_input.lower() != "exit":
        new_game.run_game()

play()