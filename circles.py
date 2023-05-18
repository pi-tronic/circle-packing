from tkinter import *
from time import sleep
from random import randint

width = 400
height = 400
colors = [
    'snow', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'light goldenrod yellow',
    'light yellow', 'yellow', 'orange', 'dark orange',
    'tomato', 'orange red',
    'red',
    'AntiqueWhite1', 'NavajoWhite2', 'yellow2', 'gold2', 'goldenrod1',
    'DarkGoldenrod1',
    'tan1', 'orange2',
    'DarkOrange1'
]

minimum = 2
maximum = 100

points = []

#### functions

def distance(x1, y1, x2, y2):
    d = ((x2-x1) **2 + (y2-y1) **2) **.5
    return d

def check(x, y):
    global points
    smallest = maximum

    for point in points:
        d = distance(x, y, point[0], point[1])

        if d-point[2]<smallest:
            smallest = d-point[2]

        if d-point[2]<minimum:
            return 0

    return smallest

# find a free spot
def find_spot():
    found = False
    trys = 0

    while not found:
        x = randint(minimum, width-minimum)
        y = randint(minimum, width-minimum)

        max_rad = check(x, y)

        if max_rad:
            found = True

        trys += 1

        if trys>50:
            return 0

    

    return x, y, max_rad

def create_new():
    global points

    x, y, rad_max = find_spot()
    r = randint(minimum, maximum)
    col = randint(0, len(colors)-1)

    if r>rad_max:
        r = rad_max

    points.append([x, y, r])

    c.create_oval(x-r, y-r, x+r, y+r, fill=colors[col])
    #c.create_oval(x-3, y-3, x+3, y+3, fill='red')



# setting up the window
root = Tk()
root.geometry(str(width)+"x"+str(height))
root.title("circles")

# setting up the canvas
c = Canvas(root,
           width=width,
           height=height,
           bg='black')
c.pack()

# creating the circles
for i in range(1000):
    create_new()
    text = c.create_text(width/2, height/2, text=i, fill='red')
    c.update()
    c.delete(text)
    sleep(.1)




# mainloop
root.mainloop()
