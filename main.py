from tkinter import *
import random

players = ["$", "#"]
player = random.choice(players)


def button_click(a, b):
    global player

    if buttons[a][b].cget('text') == "" and winner() is False:

        if player == players[0]:

            buttons[a][b].config(text=player)

            if winner() is False:

                player = players[1]
                turn_label.config(text=(players[1].upper() + ": TURN"))

            elif winner() is True:

                turn_label.config(text=(players[0].upper() + " Wins"))

            elif winner() == "Tie!":

                turn_label.config(text="Tie!")


        else:

            buttons[a][b].config(text=player)

            if winner() is False:

                player = players[0]
                turn_label.config(text=(players[0].upper() + ": TURN"))

            elif winner() is True:

                turn_label.config(text=(players[1].upper() + " Wins"))

            elif winner() == "Tie!":

                turn_label.config(text="Tie!")


def winner():
    for x in range(3):
        if buttons[x][0].cget('text') == buttons[x][1].cget('text') == buttons[x][2].cget('text') != "":
            buttons[x][0].config(bg="green")
            buttons[x][1].config(bg="green")
            buttons[x][2].config(bg="green")
            return True

    for y in range(3):
        if buttons[0][y].cget('text') == buttons[1][y].cget('text') == buttons[2][y].cget('text') != "":
            buttons[0][y].config(bg="green")
            buttons[1][y].config(bg="green")
            buttons[2][y].config(bg="green")
            return True

    if buttons[0][0].cget('text') == buttons[1][1].cget('text') == buttons[2][2].cget('text') != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2].cget('text') == buttons[1][1].cget('text') == buttons[2][0].cget('text') != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for x in range (3):
            for y in range (3):
                buttons[x][y].config(bg="yellow")
        return "Tie!"

    else:
        return False


def empty_spaces():
    spaces = 9

    for x in range(3):
        for y in range(3):

            if buttons[x][y].cget('text') == "":
                spaces -= spaces

    if spaces != 0:
        return False
    else:
        return True


def reset():
    global player

    player = random.choice(players)
    turn_label.config(text=player.upper() + ": TURN")

    for x in range(3):
        for y in range(3):
            buttons[x][y].config(text="",bg="white")


window = Tk()
window.title("TIC TAC TOE")
window.resizable(False, False)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# HEIGHT = 500
# WIDTH = 500

# window_width = window.winfo_screenwidth()
# window_height = window.winfo_screenheight()

# window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, int((window_width - WIDTH) / 2), int((window_height - HEIGHT) / 2)))

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

frame1 = Frame(window, )
frame1.grid(row=0, column=0)

turn_label = Label(frame1, text=player.upper() + ": TURN", font=('Arial', 30), bg="black", fg="white", height=2,
                   width=14)
turn_label.grid(row=0, column=0)

reset_button = Button(frame1, text='RESET', font=('Arial', 30), width=6, height=1, command=reset)
reset_button.grid(row=0, column=1)

frame2 = Frame(window)
frame2.grid(row=1, column=0)

for x in range(3):
    for y in range(3):
        buttons[x][y] = Button(frame2, text="", font=('Arial', 40), width=5, height=2, bg="white",
                               command=lambda x=x, y=y: button_click(x, y))
        buttons[x][y].grid(row=x, column=y)

window.mainloop()
