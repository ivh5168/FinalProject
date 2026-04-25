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
            [100,99,98,97,96,95,94,93,92,91],
            [81,82,83,84,85,86,87,88,89,90],
            [80,79,78,77,76,75,74,73,72,71],
            [61,62,63,64,65,66,67,68,69,70],
            [60,59,58,57,56,55,54,53,52,51],
            [41,42,43,44,45,46,47,48,49,50],
            [40,39,38,37,36,35,34,33,32,31],
            [21,22,23,24,25,26,27,28,29,30],
            [20,19,18,17,16,15,14,13,12,11],
            [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
            ]
        
        self.snakes = snakes
        self.ladders = ladders

    def display_board(self):
        for row in self.board:
            print(row)

    def roll_dice(self):
        result = random.randint(1, 6)

        return result

    def update_board(self):
        pass

    def clear_screen(self):
        print("\033[H\033[J", end="")  # ANSI escape sequence for clearing screen

    def run_game(self):
        

        player_input = input("Welcome to Snakes and Ladders!\nInput anything (but 'Quit' or 'Exit') to continue: \n")
        if player_input.lower() != "quit" and player_input.lower() != "exit":
            self.clear_screen
            count = 1
            while player_input.lower() != "quit" and player_input.lower() != "exit":
                self.clear_screen
                self.display_board()
                player_input = input("\nRoll dice?")

                if player_input.lower() != "quit" and player_input.lower() != "exit":
                    roll = self.roll_dice()
                    
                    if count % 2 == 0:
                        turn = 2
                        p2_pos += roll
                    else:
                        turn = 1
                        p1_pos += roll

                    count += 1
                    
                    time.sleep(1)

                    print(f"Player {turn} rolled a {roll}\n")

                    time.sleep(3)

def play():
    new_game = Game()
    new_game.run_game()

play()