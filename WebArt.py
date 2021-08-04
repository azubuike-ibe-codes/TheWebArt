from tkinter import *
import math as m


class Window(Frame):
    N = 30  # Number of nodes
    W = 800  # Width of window
    H = 800  # Height of window
    R = min(W, W) / 2.2  # Radius of wheel
    X0 = (W / 2, H / 2)  # Tuple center of wheel

    def __init__(s, master=None) :
        Frame.__init__(s, master)
        s.master = master
        s.canv = Canvas(width=s.W, height=s.H)
        s.canv.pack()
        s.wheel()

    def wheel(s):
        a = [i * m.pi * 2 / s.N for i in range(s.N)]
        x = [(s.X0[0] + s.R * m.cos(a[i], s.X0[1] + s.R * m.sin(a[i])) for i in range(s.N) )]
        for i in range(s.N - 1):
            for j in range(i + 1, s.N):
                s.canv.create_line(x[i][0], x[i][1], x[j][0], x[j][1])


root = Tk()
app = Window(root)
root.mainloop()
