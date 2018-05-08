from tkinter import *


class Example(Frame):
    x0 = y0 = 0
    x1 = 800
    y1 = 532
    h = 25

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def moveLeft(self, c):
        if self.x0 - self.h >= 0:
            c.move("img", -self.h, 0)
            self.x0 -= self.h
            self.x1 -= self.h
        elif self.x0 > 0:
            t = -self.x0
            c.move("img", t, 0)
            self.x0 = 0
            self.x1 += t

    def moveRight(self, c):
        if self.x1 + self.h <= 1200:
            c.move("img", self.h, 0)
            self.x0 += self.h
            self.x1 += self.h
        elif self.x1 < 1200:
            t = 1200 - self.x1
            c.move("img", t, 0)
            self.x0 += t
            self.x1 += t

    def moveUp(self, c):
        if self.y0 - self.h >= 0:
            c.move("img", 0, -self.h)
            self.y0 -= self.h
            self.y1 -= self.h
        elif self.y0 > 0:
            t = -self.y0
            c.move("img", 0, t)
            self.y0 = 0
            self.y1 += t

    def moveDown(self, c):
        if self.y1 + self.h <= 700:
            c.move("img", 0, self.h)
            self.y0 += self.h
            self.y1 += self.h
        elif self.y1 < 700:
            t = 705 - self.y1
            c.move("img", 0, t)
            self.y0 += t
            self.y1 += t

    def initUI(self):
        self.parent.title("RB")
        self.pack(fill=BOTH, expand=1)

        c = Canvas(self)
        c.bind("<1>", lambda event: c.focus_set())
        c.bind('<Key-Left>', lambda x: self.moveLeft(c))
        c.bind('<Key-Right>', lambda x: self.moveRight(c))
        c.bind('<Key-Up>', lambda x: self.moveUp(c))
        c.bind('<Key-Down>', lambda x: self.moveDown(c))

        c.pack(fill=BOTH, expand=1)

        c.create_rectangle(0, 0, 800, 177, fill="#0075eb", outline="#0075eb", tag="img")
        c.create_rectangle(0, 356, 800, 532, fill="green", outline="green", tag="img")

        c.create_oval(334, 200, 466, 332, outline="#ffd700", width="8", tag="img")

        c.create_oval(386, 252, 414, 280, fill="#ffd700", outline="#ffd700", tag="img")

        c.create_oval(348, 258, 364, 274, fill="#ffd700", outline="#ffd700", tag="img")
        c.create_oval(354, 236, 370, 252, fill="#ffd700", outline="#ffd700", tag="img")
        c.create_oval(370, 220, 386, 236, fill="#ffd700", outline="#ffd700", tag="img")
        c.create_oval(392, 214, 408, 230, fill="#ffd700", outline="#ffd700", tag="img")
        c.create_oval(414, 220, 430, 236, fill="#ffd700", outline="#ffd700", tag="img")
        c.create_oval(431, 236, 447, 252, fill="#ffd700", outline="#ffd700", tag="img")
        c.create_oval(437, 258, 453, 274, fill="#ffd700", outline="#ffd700", tag="img")

        c.create_line(356, 266, 445, 266, fill="#ffd700", width="4", tag="img")
        c.create_line(362, 244, 400, 266, fill="#ffd700", width="4", tag="img")
        c.create_line(378, 228, 400, 266, fill="#ffd700", width="4", tag="img")
        c.create_line(400, 222, 400, 311, fill="#ffd700", width="4", tag="img")
        c.create_line(422, 228, 400, 266, fill="#ffd700", width="4", tag="img")
        c.create_line(439, 244, 400, 266, fill="#ffd700", width="4", tag="img")

        moveXleft_btn = Button(self, text="◄", font=10, width=4, command=lambda: self.moveLeft(c))
        moveXleft_btn.pack(side="left", fill=BOTH)
        moveXright_btn = Button(self, text="►", font=10, width=4, command=lambda: self.moveRight(c))
        moveXright_btn.pack(side="right", fill=BOTH)
        moveYup_btn = Button(self, text="▲", font=10, height=2, command=lambda: self.moveUp(c))
        moveYup_btn.pack(side="top", fill=BOTH)
        moveYdown_btn = Button(self, text="▼", font=10, height=2, command=lambda: self.moveDown(c))
        moveYdown_btn.pack(side="bottom", fill=BOTH)


root = Tk()
ex = Example(root)
root.geometry("1200x800+250+10")
root.minsize(1200, 800)
root.maxsize(1200, 800)
root.mainloop()