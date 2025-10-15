# from turtle import Turtle, Screen
#
# donatello = Turtle()
#
# my_screen = Screen()
# my_screen.canvheight
# print(my_screen.canvwidth)
# donatello.shape("turtle")
# donatello.color("purple")
#
# donatello.forward(500)
#
# my_screen.exitonclick()
#
# print(donatello)

from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column("Name", ["Schmeichel", "Neville", "Stam", "Ferdinand", "Irwin", "Ronaldo", "Keane", "Scholes", "Giggs", "Cantona", "Rooney"])

my_table.add_column("Position", ["GK", "RB", "CB", "CB", "LB", "RW", "CM", "CM", "LM", "ST", "ST"])

my_table.add_column("Number", [1, 2, 6, 5, 3, 7, 16, 18, 11, 7, 10])

# my_table.align = "l"
my_table.align["Name"] = "l"
my_table.header_style = "upper"

my_table.add_row(["Ferguson", "MGR", "N/A"])

print(my_table.align)

print(my_table)