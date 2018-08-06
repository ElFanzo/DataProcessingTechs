from tkinter import Tk, Frame, Scale, Label
from bs4 import BeautifulSoup
from requests import get


class Palette(Frame):
    """
    Palette class implementation.
    """
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.name = None
        self.label = None
        self.colors = {}
        self.r = 0
        self.g = 0
        self.b = 0
        self.getColors()
        self.run()

    def change(self):
        """
        Label color changing.
        """
        r, g, b = map(int, (self.r, self.g, self.b))
        color = '#%s%s%s' % (hex(r)[2:].zfill(2), hex(g)[2:].zfill(2), hex(b)[2:].zfill(2))
        self.label.configure(bg=color)
        try:
            self.name.configure(text=self.colors[color])
        except KeyError:
            self.name.configure(text=color)

    def changeRed(self, val):
        self.r = val
        self.change()

    def changeGreen(self, val):
        self.g = val
        self.change()

    def changeBlue(self, val):
        self.b = val
        self.change()

    def run(self):
        self.pack()

        label = Label(self, bg='black', height=20, width=40)
        label.pack()
        name = Label(self, text='black')
        name.pack()
        self.name = name
        self.label = label

        red = Scale(self, from_=0, to=255, orient='horizontal', length=256, label='Red', command=self.changeRed)
        red.pack()

        green = Scale(self, from_=0, to=255, orient='horizontal', length=256, label='Green', command=self.changeGreen)
        green.pack()

        blue = Scale(self, from_=0, to=255, orient='horizontal', length=256, label='Blue', command=self.changeBlue)
        blue.pack()

    def getColors(self):
        """
        Getting a list of color names.
        """
        req = get('http://www.color-hex.com/color-names.html')
        bs = BeautifulSoup(req.content, 'html5lib')

        rows = bs.find('div', class_='content').find('table').find_all('tr')

        for row in rows[1:]:
            name = row.find('td').text
            hex = row.find_all('td')[2].text
            self.colors[hex] = name


if __name__ == '__main__':
    master = Tk()
    master.maxsize(350, 550)
    master.minsize(350, 550)
    master.title('Palette')
    palette = Palette(master)
    master.mainloop()