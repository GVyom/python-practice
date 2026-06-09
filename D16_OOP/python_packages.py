#PyPI: Library for already written code -> research and use as and when needed
#Unlike Turtle, a lot of files are needed to be installed
from prettytable import PrettyTable
table = PrettyTable() 
table.add_column("Pokemon",["Pikachu", "Squirtle", "Balbasaur","Charmander"])
table.add_column("type", ["Electirc", "Water", "Grass","Fire"])
table.align = "l"
table.border = False
print(table)

