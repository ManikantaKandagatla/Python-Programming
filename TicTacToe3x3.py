__author__ = 'ManiKanta Kandagatla'

import simpleguitk as simplegui
from ttk import *
from Tkinter import *

# Handler to draw on canvasg

flag = 1

def free_contents():
    for x in range(3):
        for y in range(3):
            btn[x][y].config(text="")
            btn[x][y]._value=-5
    val = [[0,0,0],[0,0,0],[0,0,0]]


def check_end_of_game():
    for x in range(3):
        sum_col = sum_row = 0
        for y in range(3):
            sum_row =  sum_row + btn[x][y]._value
            sum_col = sum_col + btn[y][x]._value
        if sum_col == 0 or sum_row ==0 :
            message.after(12,"0 won the game")
            print "0 won the game"
            free_contents()
        elif sum_col == 3  or sum_row ==3:
            message.after(12,"1 won the game")
            print "1 won the game"
            free_contents()
        x = 0
        sum_diag_left = sum_diag_right = 0
    while x < 3:
        sum_diag_left = sum_diag_left + btn[x][x]._value
        sum_diag_right = sum_diag_right +btn[2-x][2-x]._value
        x = x+1
    if sum_diag_left ==0 :
        message.after(12,"0 won the game")
        print "0 won the game"
        free_contents()
    elif sum_diag_right ==3:
        message.after(12,"1 won the game")
        print "1 won the game"
        free_contents()

def color_change(x,y):
    global flag
    if val[x][y] == 0 :
        btn[x][y].config(text=str(flag))
        btn[x][y]._value = flag
        print btn[x][y]._value
        val[x][y]=1
        check_end_of_game()
        if flag == 0:
            flag = 1
        else:
            flag = 0

# Create a frame and assign callbacks to event handlers
root = Tk()
frame = Frame(root)
frame.grid(row=0,column=0)
message = Label(frame,text="Result")
message.grid(column=0,row =0)
val =[[0,0,0],[0,0,0],[0,0,0]]
btn=  [[0 for x in xrange(3)] for x in xrange(3)]
for x in range(3):
    for y in range(3):
        btn[x][y] = Button(frame,command= lambda x1=x, y1=y: color_change(x1,y1))
        btn[x][y].grid(column=x+1, row=y+1)
        btn[x][y].config(height=10,width=10,bg="blue")
        btn[x][y]._value=-5
#frame = simplegui.create_frame("Home", 200, 200)

root.mainloop()
#frame.start()




