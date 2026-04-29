import random, time

class Player:
    def __init__(self, id):
        self.id = id
        self.pos = (9, 0) # Player coordinates formated: row, column
        self.int_pos = 1
        self.has_won = False

    def update_position(self, roll):
        row_pos = self.pos[0]
        col_pos = self.pos[1]
        
        if self.int_pos + roll <= 100: # If player does not overshoot 100
            col_pos += roll
            self.int_pos += roll

        # Updates player coordinates if they made it to a upper row
        if col_pos > 9:
            row_pos -= 1
            col_pos -= 10

        self.pos = (row_pos, col_pos) # Updates player coordinates

        if self.int_pos == 100: # If the player reaches the end and wins.
            self.has_won = True

    def hit_snake(self, new_int, new_pos):
        print(f"Player {self.id} hit a snake! {self.int_pos} -> {new_int}")
        self.int_pos = new_int
        self.pos = new_pos

    def hit_ladder(self, new_int, new_pos):
        print(f"Player {self.id} got to a ladder! {self.int_pos} -> {new_int}")
        self.int_pos = new_int
        self.pos = new_pos

class Game:
    def __init__(self, 
        board = [
            ["91_L7","92_S6","93","94","95_S7","96","97","98_S8","99_L8","100"],
            ["81","82","83","84_L5","85","86","87_S5","88","89","90"],
            ["71","72_L7","73_S6","74","75_S7","76","77","78","79_S8","80_L8"],
            ["61","62_S3","63","64_S4","65","66","67_L6","68","69","70"],
            ["51_L6","52","53","54_S2","55","56","57","58","59","60"],
            ["41_S4","42_L4","43","44","45","46","47","48","49","50"],
            ["31","32","33","34_S2","35","36_S5","37","38_L1","39","40"],
            ["21_L4","22","23","24","25","26","27","28_L5","29","30_L3"],
            ["11","12","13","14_L2","15","16","17_S1","18_S3","19","20"],
            ["1","2_L1","3","4_L2","5","6","7_S1","8","9_L3","10"]
        ],
        # Formatted top of snake: bottom of snake (coords)
        snakes = {
        17: (7, (9, 6)),
        54: (34, (6, 3)),
        62: (18, (8, 7)),
        64: (41, (5, 0)),
        87: (36, (6, 5)),
        92: (73, (2, 2)),
        95: (75, (2, 4)),
        98: (79, (2, 8))
        }, 
        # Formatted bottom of ladder: top of ladder (coords)
        ladders = {
        2: (38, (6, 7)),
        4: (14, (8, 3)),
        9: (30, (7, 9)),
        21: (42, (5, 1)),
        28: (84, (1, 3)),
        51: (67, (3, 6)),
        72: (91, (0, 0)),
        80: (99, (0, 8))
        }
        ):
        self.board = board
        self.snakes = snakes
        self.ladders = ladders
        self.turns = 1 # Keeps track of how many turns have passed.

    def display_board(self, p1, p2):
        disp_board = self._format_board(p1, p2)
        
        for row in disp_board:
            print(row)

    def _format_board(self, p1, p2):
        # Formats rows so even rows are in displayed in reverse.
        disp_board = []
        for i in range(len(self.board)):
            row = self.board[i][:] # Creates a copy of the row
            # Displays player coordinates by adding them to the display board
            for j in range(len(row)):
                if i == p2.pos[0] and j == p2.pos[1]: # If i and j equal player one's coords
                    row[j] = "P2_" + row[j]
                if i == p1.pos[0] and j == p1.pos[1]: # If i and j equal player one's coords
                    row[j] = "P1_" + row[j]

            # Adds row to board
            if i % 2 == 0: # Even row
                row = list(reversed(row)) # Reverses the board to match proper Snakes and Ladders board
                disp_board.append(row)
            else: # Odd row 
                disp_board.append(row)

        return disp_board

    def roll_dice(self):
        result = random.randint(1, 6)

        return result

    def clear_screen(self):
        print("\033[H\033[J", end="")  # ANSI escape sequence for clearing screen

    def determine_turn(self):
        if self.turns % 2 == 0:
            turn = 2
        else:
            turn = 1
        
        return turn

    def run_game(self):
        try:
            player_input = input("Enter 'Quit' or 'Exit' to end program at any time. ")
        except Exception:
            player_input = ""
            print("Please input valid argument next time.")

        player_one = Player("1")
        player_two = Player("2")
        
        self.clear_screen()
        
        turn = 1 # 1 - Player one's turn. 2 - Player two's turn.

        while player_input.lower() != "quit" and player_input.lower() != "exit" and player_one.has_won == False and player_two.has_won == False:
            # Update screen
            self.clear_screen()
            self.display_board(player_one, player_two)
            print(f"\nPlayer One: {player_one.int_pos}\nPlayer Two: {player_two.int_pos}")

            # Determine player turn
            turn = self.determine_turn()

            try:
                player_input = input(f"\nPlayer {turn} roll dice?")
            except Exception:
                player_input = ""
                print("Please input valid argument next time.")
            
            if player_input.lower() != "quit" and player_input.lower() != "exit": # If player chooses to not exit
                roll = self.roll_dice()
                
                if turn == 1: # If player one's turn
                    player_one.update_position(roll)

                    if player_one.int_pos in self.snakes: # If player one hit a snake
                        # Gets new player positions
                        new_int = self.snakes[player_one.int_pos][0]
                        new_pos = self.snakes[player_one.int_pos][1]

                        player_one.hit_snake(new_int, new_pos)
                    elif player_one.int_pos in self.ladders: # If player one hit a ladder
                        # Gets new player positions
                        new_int = self.ladders[player_one.int_pos][0]
                        new_pos = self.ladders[player_one.int_pos][1]

                        player_one.hit_ladder(new_int, new_pos)
                else: # turn == 2 # If player two's turn
                    player_two.update_position(roll)

                    if player_two.int_pos in self.snakes: # If player two hit a snake
                        # Gets new player positions
                        new_int = self.snakes[player_two.int_pos][0]
                        new_pos = self.snakes[player_two.int_pos][1]

                        player_two.hit_snake(new_int, new_pos)
                    elif player_two.int_pos in self.ladders: # If player two hit a ladder
                        # Gets new player positions
                        new_int = self.ladders[player_two.int_pos][0]
                        new_pos = self.ladders[player_two.int_pos][1]

                        player_two.hit_ladder(new_int, new_pos)
                    
                self.turns += 1
                
                time.sleep(2)

                # Update screen
                self.clear_screen()
                self.display_board(player_one, player_two)
                print(f"\nPlayer One: {player_one.int_pos}\nPlayer Two: {player_two.int_pos}")
                print(f"\nPlayer {turn} rolled a {roll}")

                time.sleep(3)

        # If game ended by someone winning.
        if player_one.has_won:
            self.clear_screen()
            print("Player one has won!")
            self.offer_replay()
        elif player_two.has_won:
            self.clear_screen()
            print("Player two has won!")
            self.offer_replay()

    def offer_replay(self):
        try:
            player_input = input("Play again? (y/n)")
        except Exception:
            player_input = ""
            print("Please input valid argument next time.")
        
        if player_input.lower() == "y": # Restarts game
            play()
        elif player_input.lower() != "n": # Invalid input
            print("Invalid input")
            self.clear_screen()
            self.offer_replay()
        # Else code finishes and program ends
    

def play():
    new_game = Game() # Creates new game

    new_game.clear_screen()

    try:
        player_input = input("Welcome to Snakes and Ladders!\nInput anything (but 'Quit' or 'Exit') to continue: \n")
    except Exception:
        player_input = ""
        print("Please input valid argument next time.")

    if player_input.lower() != "quit" and player_input.lower() != "exit":
        new_game.run_game()

play()