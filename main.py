from tkinter import *
from tkinter import messagebox, ttk
import game_logic
from database import get_result

#Function to start the game
def start_button_function ():
    if (valid_input_check()):
        game_logic.game_initialisation(str(name_value.get()), int(diff_value.get()), int(lenx_value.get()), int(leny_value.get()), int(width_value.get()))
    else:
        show_error_window()

def info_button_function ():
    messagebox.showinfo("Menu info", 'Horizontal – number of cells by horizontal axis (from five to twenty four)\n\n'
                                     'Vertical – number of cells by vertical axis (from five to twenty four)\n\n'
                                     'Width – width of cells (from fifteen to eighty)\n\n'
                                     'Difficulty – speed of snake (from one to ten)\n\n'
                                     'Name – name of player played game')

def valid_input_check ():
    variables_to_check = [diff_value.get(), lenx_value.get(), leny_value.get(), width_value.get()]
    for i in range (0, len(variables_to_check)):
        try:
            variables_to_check[i] = int(variables_to_check[i])
        except ValueError:
            return False
        if (i == 0):
            if (variables_to_check[i] < 1 or variables_to_check[i] > 10):
                return False
        elif (i == 3):
            if (variables_to_check[i] < 15 or variables_to_check[i] > 80):
                return False
        else:
            if (variables_to_check[i] < 5 or variables_to_check[i] > 24):
                return False
    return True

def show_error_window ():
    messagebox.showerror('Invalid data', 'You have entered invalid data.\n'
                                         'Please, check information about limitations\n'
                                         'in "info" button and then try again')

def highscore_button_function():
    highscores_window = Tk()
    highscores_window.title('Highscores')
    #highscores_window.geometry('300x300')

    results = get_result()
    columns = ('num', 'name', 'score')

    tree = ttk.Treeview(highscores_window, columns = columns, show = 'headings')
    tree.pack(fill=BOTH, expand=1)

    tree.heading('num', text = 'Attempt №')
    tree.heading('name', text = 'Name')
    tree.heading('score', text = 'Score')

    for _game in results:
        tree.insert('', END, values = _game)

    highscores_window.mainloop()

#These variables we need to tune window, game and playground
current_score = 0 #score increases with devouring fruits

root = Tk() #creating our window

#Here we put some settings on our window
root.title('Main menu')
root.geometry('500x200')


title_label = Label(text = 'Snake', font=30, background = 'lightgray')
title_label.grid(row = 0, column = 1, columnspan=2, pady = 10)


lenx_label = Label(text = 'Horizontal: ', padx = 10, pady = 10)
lenx_label.grid(row = 1, column = 0)
#
lenx_value = StringVar()
lenx_entry = Entry(root, textvariable = lenx_value)
lenx_entry.grid(row = 1, column = 1)
#
leny_label = Label(text = 'Vertical: ', padx = 10, pady = 10)
leny_label.grid(row = 1, column = 2)
#
leny_value = StringVar()
leny_entry = Entry(root, textvariable = leny_value)
leny_entry.grid(row = 1, column = 3)


diff_label = Label(text = 'Difficulty: ', padx = 10, pady = 10)
diff_label.grid(row = 2, column = 0)
#
diff_value = StringVar()
diff_entry = Entry(root, textvariable = diff_value)
diff_entry.grid(row = 2, column = 1)
#
width_label = Label(text = 'Width: ', padx = 10, pady = 10)
width_label.grid(row = 2, column = 2)
#
width_value = StringVar()
width_entry = Entry(root, textvariable = width_value)
width_entry.grid(row = 2, column = 3)


name_label = Label(text = 'Name: ', padx = 10, pady = 10)
name_label.grid(row = 3, column = 2)
#
name_value = StringVar()
name_entry = Entry(root, textvariable = name_value)
name_entry.grid(row = 3, column = 3)


info_button = Button(root, command = info_button_function, text = 'Info')
info_button.grid(row = 4, column = 0, padx = 10, pady = 10)
#
start_button = Button(root, command = start_button_function, text = 'Start!')
start_button.grid(row = 4, column = 1, padx = 10, pady = 10)
#
highscore_button = Button(root, command = highscore_button_function, text = 'Highscores')
highscore_button.grid(row = 4, column = 2, padx = 10, pady = 10)

root.mainloop() #we need this to make window appear and functionising

#First part is the Red cube
#Second part is the nice grid
#Third part is to make cube move by punching the buttons
#Fourth part is to make cube teleport on the opposite side of location if he move into the wall
#Fifth part is to give snake a tail
#Sixth part is to make snake mortal
#Seventh part is to make fruits grow and make snake eat them and became longer
#Eight part is to make code look nicer
#Ninght part is to make snake move by itself
#Tenth part is to separate code by modules
#Eleventh part is to make nice main menu and make all vidgets work
#Twelfth part is to execute program from side computer
#Twelfth part is to connect project with the database
#Trirteenth step is to develop other's ideas (borderless field, different levels, etc.)