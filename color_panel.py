from tkinter import Frame, Label, Scale, Tk

from grab import Grab


class Palette(Frame):
    """Palette class implementation."""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.name = None
        self.label = None
        self.colors = {}
        self.r = 0
        self.g = 0
        self.b = 0
        self.get_colors()
        self.run()

    def change(self):
        """Change the color's label."""
        r, g, b = map(int, (self.r, self.g, self.b))
        color = "#%s%s%s" % (
            hex(r)[2:].zfill(2),
            hex(g)[2:].zfill(2),
            hex(b)[2:].zfill(2),
        )
        self.label.configure(bg=color)
        try:
            self.name.configure(text=self.colors[color])
        except KeyError:
            self.name.configure(text=color)

    def change_red(self, val):
        """Change the shade of red color."""
        self.r = val
        self.change()

    def change_green(self, val):
        """Change the shade of green color."""
        self.g = val
        self.change()

    def change_blue(self, val):
        """Change the shade of blue color."""
        self.b = val
        self.change()

    def run(self):
        self.pack()

        label = Label(self, bg="black", height=20, width=40)
        label.pack()
        name = Label(self, text="black")
        name.pack()
        self.name = name
        self.label = label

        red = Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            length=256,
            label="Red",
            command=self.change_red,
        )
        red.pack()

        green = Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            length=256,
            label="Green",
            command=self.change_green,
        )
        green.pack()

        blue = Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            length=256,
            label="Blue",
            command=self.change_blue,
        )
        blue.pack()

    def get_colors(self):
        """Get a list of color names."""
        g = Grab(transport="urllib3")
        g.go("http://www.color-hex.com/color-names.html")

        rows = g.doc.select("/html/body/div[2]/div/table/tr")
        for row in rows[1:]:
            name = row.select("td[1]").text()
            _hex = row.select("td[3]").text()
            self.colors[_hex] = name


if __name__ == "__main__":
    master = Tk()
    master.maxsize(350, 550)
    master.minsize(350, 550)
    master.title("Palette")
    palette = Palette(master)
    master.mainloop()
