"This program is a tic-tac-toe GUI"
"Created by Nancy Donathan"
"Latest revision date is 12/12/2021"

from tkinter import *

from tkinter import messagebox

import tkinter as tk

#This section opens up a welcome window when the game is first opened
splashWin = Tk()
welcomeImage = tk.PhotoImage(file = 'welcome.png') #This is the image
splashWin.title("Welcome") #This is the title of the window
splashWin.geometry("200x200") #This is the size of the window
splashLabel = Label(splashWin, image = welcomeImage).pack() #This adds the image

#This is the section that starts the game
root = Tk()
root.title("Tic-Tac-Toe") #This is the title of the game window
root.iconbitmap('icon.ico') #This adds an icon image

clicked = True
count = 0

#This defines the quit game section
def quitGame():
    global root
    msg = messagebox.askquestion("Confirm", "Are you sure you want to quit?") #This adds a message box
    if msg == "yes":
        root.destroy() #This closes the window if the user chooses 'yes'

#This section defines the disable buttons function
def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

#This section defines the section that checks if a player won
def checkifwon():
    global winner
    winner = False

    #This section checks each row to see if they meet any of the winning conditions (All following code definitions are the same for each section in the checkifwon def unless stated otherwise)
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X": 
        b1.config(bg = "red") #This turns the background red if 'X' wins
        b2.config(bg = "red")
        b3.config(bg = "red")
        winner = True #This changes the winning condition to true if all the conditions are met
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!") #This brings up a message box telling the player they won
        disable_all_buttons() #This calls back the function to disable the buttons

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "red")
        b5.config(bg = "red")
        b6.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "red")
        b8.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "red")
        b4.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "red")
        b5.config(bg = "red")
        b8.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "red")
        b6.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "red")
        b5.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "red")
        b5.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations X! You win!")
        disable_all_buttons()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "green") #This turns the background green if 'O' wins
        b2.config(bg = "green")
        b3.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "green")
        b5.config(bg = "green")
        b6.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "green")
        b8.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "green")
        b4.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "green")
        b5.config(bg = "green")
        b8.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "green")
        b6.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "green")
        b5.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "green")
        b5.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations O! You win!")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie\nNo one wins")
        disable_all_buttons()

#This section checks to see which buttons have been clicked
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count +=1
        checkifwon()
        
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "You can not select that box\nThat box has already been selected\nPlease pick another box")

#This section creates and resets the buttons of the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b1)) #This creates each individual button setting the height, font, and color
    b2 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b2))
    b3 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b3))

    b4 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b4))
    b5 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b5))
    b6 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b6))

    b7 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b7))
    b8 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b8))
    b9 = Button(root, text=" ", font = ("Times", 20), height = 3, width = 6, bg = "grey", command = lambda: b_click(b9))


    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

#This section creates the menu
myMenu = Menu(root)
root.config(menu = myMenu)

optionsMenu = Menu(myMenu, tearoff = False)
myMenu.add_cascade(label = "Options", menu=optionsMenu)
optionsMenu.add_command(label="New Game", command = reset)
optionsMenu.add_command(label = "Quit", command = quitGame)

reset()

#This section is the mainloop
root.mainloop()

