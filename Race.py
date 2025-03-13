from graphics import *
from graphics import GraphWin, Line, Image, Point, update
from random import randint
import time
from Dice import Dice

class Horse:
    def __init__(self, speed, y, image_file, window):
        self.x_pos = 50  # starting point
        self.y_pos = y  # track
        self.image_file = image_file
        self.image = Image(Point(self.x_pos, self.y_pos), image_file)  # creating image
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        step = self.dice.roll()
        self.x_pos += step
        self.image = Image(Point(self.x_pos, self.y_pos), self.image_file)

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_x):
        if self.x_pos >= finish_x:
            return True
        else:
            return False

def main():
    win = GraphWin("Horse Race", 700, 350, autoflush=False)
    win.setBackground("green")

    horse1 = Horse(6, 100, "../A2/horse1.gif", win)
    horse2 = Horse(6, 200, "../A2/horse2.gif", win)

    finish_line = Line(Point(600, 50), Point(600, 300))
    finish_line.setWidth(3)
    finish_line.draw(win)

    horse1.draw()
    horse2.draw()

    win.getMouse()  # starting race

    while True:
        win.delete("all")

        finish_line.undraw()
        finish_line.draw(win)

        horse1.move()
        horse2.move()

        horse1.draw()
        horse2.draw()

        update(30)

        if horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600):
            print("Tie")
            break
        elif horse1.crossed_finish_line(600):
            print("Horse 1 is the winner")
            break
        elif horse2.crossed_finish_line(600):
            print("Horse 2 is the winner")
            break

    print("Click the mouse to close.")
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
