def display(r1, r2, r3):
    print(f"{r1}\n{r2}\n{r3}")


class player:

    def __init__(self, marker, name):
        self.marker = marker
        self.name = name

    def place_parker(self, place):
        if place == 1:
            if row3[0] != "X" and row3[0] != "O":
                row3[0] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 2:
            if row3[1] != "X" and row3[1] != "O":
                row3[1] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 3:
            if row3[2] != "X" and row3[2] != "O":
                row3[2] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 4:
            if row2[0] != "X" and row2[0] != "O":
                row2[0] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 5:
            if row2[1] != "X" and row2[1] != "O":
                row2[1] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 6:
            if row2[2] != "X" and row2[2] != "O":
                row2[2] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 7:
            if row1[0] != "X" and row1[0] != "O":
                row1[0] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 8:
            if row1[1] != "X" and row1[1] != "O":
                row1[1] = self.marker
            else:
                print("You miss your turn for trying that!")
        elif place == 9:
            if row1[2] != "X" and row1[2] != "O":
                row1[2] = self.marker
            else:
                print("You miss your turn for trying that!")


def check(r1, r2, r3):
    if r3[0] == "O" and r3[1] == "O" and r3[2] == "O":
        return "O"
    elif r2[0] == "O" and r2[1] == "O" and r2[2] == "O":
        return "O"
    elif r1[0] == "O" and r1[1] == "O" and r1[2] == "O":
        return "O"
    elif r1[0] == "O" and r2[1] == "O" and r3[2] == "O":
        return "O"
    elif r3[0] == "O" and r2[1] == "O" and r1[2] == "O":
        return "O"
    elif r3[0] == "X" and r3[1] == "X" and r3[2] == "X":
        return "X"
    elif r2[0] == "X" and r2[1] == "X" and r2[2] == "X":
        return "X"
    elif r1[0] == "X" and r1[1] == "X" and r1[2] == "X":
        return "X"
    elif r1[0] == "X" and r2[1] == "X" and r3[2] == "X":
        return "X"
    elif r3[0] == "X" and r2[1] == "X" and r1[2] == "X":
        return "X"
    elif r1[0] != " " and r1[1] != " " and r1[2] != " " and r2[0] != " " and r2[1] != " " and r2[2] != " " and r3[0] != " " and r3[1] != " " and r3[2] != " ":
        return "draw"
    else:
        return None
    
    
print("Welcome to Tic Tac Toe by MilosK\n")
print("Make sure your num lock is set on numeric!\n")
input("Press enter to start:")
game = "ON"
in1 = input("X players name: ")
in2 = input("O players name: ")
while game == "ON":
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    Xp = player("X", in1)
    Yp = player("O", in2)
    display(row1, row2, row3)
    while True:
        place = int(input(f"{in1}, place your marker as a num lock number (X): "))
        Xp.place_parker(place)
        result = check(row1, row2, row3)
        display(row1, row2, row3)
        if result == None:
            pass
        elif result == "draw":
            print("Its a draw!!")
            break
        elif result == "X":
            print(f"{in1} won as X")
            break
        place = int(input(f"{in2}, place your marker as a num lock number (Y): "))
        Yp.place_parker(place)
        result = check(row1, row2, row3)
        display(row1, row2, row3)
        if result == None:
            pass
        elif result == "draw":
            print("Its a draw!!")
            break
        elif result == "O":
            print(f"{in2} won as O")
            break

    cont = input("Capital Y for another round, capital N for the game to end: ")
    if cont == "Y":
        continue
    else:
        print("Thanks for playing!")
        game == "OFF"
        break  

print("(You will need to rerun the script to play again)")  