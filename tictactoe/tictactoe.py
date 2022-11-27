import random
from tkinter import *


def next_turn(row, column):

    global player
    if btn[row][column]['text'] == '' and check_winner() is False:
        if joueur == joueurs[0]:
            btn[row][column]['text'] = joueur

            if check_winner() is False:
                joueur = joueurs[1]
                label.config(text=(joueurs[1] + ' tour'))

            elif check_winner() is True:
                label.cofing(text=(joueurs[0] + ' gg'))
            elif check_winner() == 'Tie':
                label.config(text=('Draw !!!'))
        else:
            btn[row][column]['text'] = joueur
            if check_winner() is False:
                joueur = joueurs[0]
                label.config(text=(joueurs[0] + ' tour'))

            elif check_winner() is True:
                label.cofing(text=(joueurs[1] + ' gg'))
            elif check_winner() == 'Tie':
                label.config(text=('Draw !!!'))


def check_winner():
    pass


def vide():
    pass


def new_game():
    pass


# def fenetre du jeux
fen = Tk()
fen.title('Tic|Tac|Toe')
joueurs = ['j1', 'j2']
joueur = random.choice(joueurs)
btn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
label = Label(text=joueur + ' ' + 'tour', font=40)
label.pack(side='top')
reset_btn = Button(text='recommencer', font=40, command=new_game)
reset_btn.pack(side='top')

frame = Frame(fen)
frame.pack()

for row in range(3):
    for column in range(3):
        btn[row][column] = Button(frame, text='', font=40, width=20,
                                  height=7, command=lambda row=row, column=column: next_turn(row, column))
        btn[row][column].grid(row=row, column=column)
fen.mainloop()
