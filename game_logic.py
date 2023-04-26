from tkinter import *
from tkinter import messagebox
from random import randint, random
from database import add_row

#####Block of different functions

#Function to record new result into database
def write_to_db():
    add_row(player_name, current_score)

#Function to make our snake bigger and longer
def tail_expansion(canvas):
    global tail
    positionx = tail[len(tail) - 1]['positionx']
    positiony = tail[len(tail) - 1]['positiony']
    body = canvas.create_rectangle( positionx, positiony,
                                    positionx + cell_width, positiony + cell_width,
                                    fill = 'orange')
    _tail = {'body': body, 'positionx': positionx, 'positiony': positiony}
    tail.append(_tail)

#Here we have a function that move our cube depends on its definition
def movement (canvas):
    global head, tail, is_alive, definition, last_definition

    #change position of every part of tail
    for i in range(len(tail) - 1, 0, -1):
        tail[i]['positionx'] = tail[i - 1]['positionx']
        tail[i]['positiony'] = tail[i - 1]['positiony']
    tail[0]['positionx'] = head['positionx']
    tail[0]['positiony'] = head['positiony']

    #preventing moving inside itself
    if (definition == 'up' and last_definition == 'down' or definition == 'down' and last_definition == 'up' or
            definition == 'right' and last_definition == 'left' or definition == 'left' and last_definition == 'right'):
        definition = last_definition
    else:
        last_definition = definition

    # change position of head to move it later
    if (definition == 'down'):
        head['positiony'] += cell_width
    elif (definition == 'up'):
        head['positiony'] -= cell_width
    elif (definition == 'right'):
        head['positionx'] += cell_width
    elif (definition == 'left'):
        head['positionx'] -= cell_width


    #In this part of function we kill our snake when it hits into the border of playground
    if ((head.get('positiony') < 0) or (head.get('positiony') > (leny - 1) * cell_width)
        or (head.get('positionx') < 0) or (head.get('positionx') > (lenx - 1) * cell_width)):
        is_alive = False


    # checking if snake bite something
    bite_check(canvas)

    #moving our snake
    canvas.coords(head['body'], head.get('positionx'), head.get('positiony'),
                  head.get('positionx') + cell_width, head.get('positiony') + cell_width)
    for i in range(0,len(tail)):
        canvas.coords(tail[i]['body'], tail[i].get('positionx'), tail[i].get('positiony'),
                      tail[i].get('positionx') + cell_width, tail[i].get('positiony') + cell_width)

#In this function definition changes when keyboard button is being pushed
def definition_change (event, defin):
    global definition
    definition = defin

#Killing snake when it bites itself or making another fruit when it eaten
def bite_check (canvas):
    global is_alive, current_score
    for i in range(0, len(tail)):
        if ((head['positionx'] == tail[i]['positionx']) and (head['positiony'] == tail[i]['positiony'])):
            is_alive = False
    if (head['positionx'] == fruit['positionx'] and head['positiony'] == fruit['positiony']):
        current_score += game_difficulty
        label['text'] = 'Score: ' + str(current_score)
        tail_expansion(canvas)
        canvas.delete(fruit['body'])
        fruit_func(canvas)

#in this function we create canvas as a playground
def playground_creating ():
    global snake_window, label
    # Here we create our canvas
    canvas = Canvas(snake_window, width=lenx * cell_width, height=leny * cell_width,
                    bg='white')
    canvas.focus_set()  # creates nice border around canvas
    canvas.pack()  # takes canvas inside the window

    # Here we draw nice grid
    for i in range(1, lenx):
        canvas.create_line(i * cell_width, 0, i * cell_width, leny * cell_width)
    for i in range(1, leny):
        canvas.create_line(0, i * cell_width, lenx * cell_width, i * cell_width)

    label = Label(snake_window, text = 'Push "s" to start', pady = 10)
    label.pack()

    return canvas

#in this function we create game window
def window_creating ():
    snake_window = Tk()
    # Here we put some settings on our window
    snake_window.title('Snake')
    #snake_window.geometry(f'{(lenx + 1) * cell_width}x{(leny + 1) * cell_width}')
    return snake_window

#In this function we create our snake
def snake_creating (canvas):
    global head, tail
    # In this part we create our snake's head and tail
    head['body'] = canvas.create_rectangle(head.get('positionx'), head.get('positiony'),
                                           head.get('positionx') + cell_width, head.get('positiony') + cell_width,
                                           fill='red')
    tail[0]['body'] = canvas.create_rectangle(tail[0].get('positionx'), tail[0].get('positiony'),
                                              tail[0].get('positionx') + cell_width,
                                              tail[0].get('positiony') + cell_width,
                                              fill='orange')

#Here we have a function that creates a fruit
def fruit_func (canvas):
    global fruit
    while (True):
        positionx = randint(0, lenx - 1) * cell_width
        positiony = randint(0, leny - 1) * cell_width
        if (head['positionx'] == positionx and head['positiony'] == positiony):
            continue
        is_good_pos = True
        for i in range(0, len(tail)):
            if (tail[i]['positionx'] == positionx and tail[i]['positiony'] == positiony):
                is_good_pos = False
                break
        if (is_good_pos):
            break

    body = canvas.create_rectangle( positionx, positiony,
                                              positionx + cell_width, positiony + cell_width,
                                              fill = 'green')
    _fruit = {'body': body, 'positionx': positionx, 'positiony': positiony}
    fruit = _fruit

def var_attachment (name, diff, lx, ly, cw):
    global game_difficulty, lenx, leny, cell_width, game_speed, player_name
    global is_alive, definition, last_definition, head, tail, fruit, current_score
    #
    game_difficulty = diff
    lenx = lx
    leny = ly
    cell_width = cw
    game_speed = (11 - game_difficulty) * 100  # speed of our snake
    player_name = name
    #
    is_alive = True
    definition = 'up'
    last_definition = 'up'
    head = {'positionx': lenx // 2 * cell_width, 'positiony': leny // 2 * cell_width}
    tail = [{'positionx': head['positionx'], 'positiony': head['positiony'] + cell_width}]
    fruit = {'positionx', 'positiony', 'body'}
    current_score = 0

#Function to prepare game Snake
def game_initialisation (name, diff, lx, ly, cw):
    global game_difficulty, lenx, leny, cell_width, snake_window
    #
    var_attachment(name, diff, lx, ly, cw)
    #
    snake_window = window_creating()
    snake_window.focus_set()
    #
    canvas = playground_creating() #creating canvas
    snake_creating(canvas) #creating snake
    fruit_func(canvas)  # creating fruit
    #
    #creating Start button
    canvas.bind('s', lambda c: start_game(canvas))
    #
    snake_window.mainloop()

#Function to start the game
def start_game (canvas):
    global label
    canvas.unbind('s')
    label['text'] = 'Here You Go!\nScore: ' + str(current_score)
    main(canvas)

#In this function we shall play
def main(canvas):
    global snake_window, is_alive
    canvas.bind('<Up>', lambda e, d='up': definition_change(e, d))
    canvas.bind('<Down>', lambda e, d='down': definition_change(e, d))
    canvas.bind('<Left>', lambda e, d='left': definition_change(e, d))
    canvas.bind('<Right>', lambda e, d='right': definition_change(e, d))

    # !!!!!!!!!!!MOVEMENT!!!!!!!!!!!!!!!
    if (definition != None):
        last_definition = movement(canvas)

    if (len(tail) >= leny * lenx - 1):
        messagebox.showinfo('You won!', 'You Won!')
        is_alive = False

    if (is_alive == True):
        snake_window.after(game_speed, lambda c=canvas: main(c))
    else:
        write_to_db()
        snake_window.destroy()

#####End of Block of different functions


#These variables we need to tune window, game and playground
game_difficulty = 0
lenx = 0
leny = 0
cell_width = 0
game_speed = 0 #(11 - game_diffilcity) * 100 #speed of our snake
player_name = None
current_score = 0 #score increases with devouring fruits
label = None
snake_window = None

#These things we need for game logic
is_alive = None
definition = None #can be 'up', 'down', 'left' or 'right'
last_definition = None
head = { 'positionx', 'positiony'}
tail = [ {'positionx', 'positiony'} ]
fruit = { 'positionx', 'positiony', 'body'}