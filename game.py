from turtle import Turtle
import random


class TurtleRace:
    turtles = []
    bet = ""

    def __init__(self, turtle_colors, screen):
        self.turtle_colors = turtle_colors
        self.screen = screen
        if (55 * len(self.turtle_colors)) >= 350:
            self.screen.setup(width=500, height=(55 * len(self.turtle_colors)))
        else:
            self.screen.setup(width=500, height=350)

    def set_bet(self):
        self.bet = self.screen.textinput(prompt="Choose your contender: ", title="Betting window").lower()

    def create_turtles(self):
        step = 50
        y = step * (len(self.turtle_colors) / 2)
        x = -(self.screen.window_width() / 2) + 20

        for color in self.turtle_colors:
            tmp_turtle = Turtle(shape="turtle")
            tmp_turtle.color(color)
            tmp_turtle.penup()
            tmp_turtle.setposition(x=x, y=y)
            self.turtles.append(tmp_turtle)
            y -= step

    def run(self):
        self.create_turtles()
        self.set_bet()
        winners = []
        run = True
        while run:
            for turtle in self.turtles:
                turtle.forward(random.randint(0, 10))

            for turtle in self.turtles:
                if turtle.xcor() >= ((self.screen.window_width() / 2) - 25):
                    winners.append(turtle.color()[0])

            if len(winners) > 0:
                run = False

        if len(winners) == 1:
            print(f"Winner is {winners[0]} and you chose {self.bet}.")
        else:
            print("Winners are: ", end="")
            for var in winners:
                print(var, end="")
                if winners.index(var) < (len(winners) - 2):
                    print(", ", end="")
                elif winners.index(var) == (len(winners) - 2):
                    print(" and ", end="")
            print(f" and you chose {self.bet}.")
        if self.bet in winners:
            print("\nYou win :)")
        else:
            print("\nYou loose :(")
