from tkinter import *
import time
import random as rnd


def go(x1, x2, y1, y2, r, h_x, h_y):
    while TRUE:
        x1 += h_x
        y1 += h_y
        x2 = x1 + r
        y2 = y1 + r
        time.sleep(0.03)
        c.coords("ball", x1, y1, x2, y2)
        c.update()

        if x1 < 0 or x2 > 1200:
            h_x *= -1
            x1 += h_x
            x2 += h_x
            chng_clr()
        elif y1 < 0 or y2 > 600:
            h_y *= -1
            y1 += h_y
            y2 += h_y
            chng_clr()


def chng_clr():
    clr = ["red", "orange", "yellow", "green", "blue", "black", "white"]
    c.itemconfig("ball", fill=clr[rnd.randint(0, 6)])


root = Tk()
root.maxsize(1200, 600)
c = Canvas(root, width=1200, height=600, bg="grey")
c.pack()

c.create_oval(100, 100, 200, 200, fill="black", tag="ball")
go(100, 100, 200, 200, 100, 12, 10)
root.mainloop()
