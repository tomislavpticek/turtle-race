from turtle import Screen
from game import TurtleRace

colors = ["blue", "green", "yellow", "red", "purple", "brown", "black", "orange", "pink" ,"grey", "beige"]

game = TurtleRace(colors, Screen())

game.run()

game.screen.exitonclick()

