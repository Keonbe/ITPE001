# Create Class Character with the following properties: Name, HP, Mp, Atk, Lvl
# Use init() method to assign values to object properties.
# Create 5 object/instance of the class and print all the properties in tabular format

class character:
    def __init__(self, name, HP, Mp, Atk, Lvl):
        self.name = name
        self.HP = HP
        self.Mp = Mp
        self.Atk = Atk
        self.Lvl = Lvl
        

c1 = character("John", 100, 5, 10, 1)
c2 = character("Peter", 100, 5, 10, 1)
c3 = character("Joseph", 100, 5, 10, 1)
c4 = character("Mary", 100, 5, 10, 1)
c5 = character("Christian", 100, 5, 10, 1)
print("CHARACTER NAME: \tHP \tMP \tATK \tLVL")
print(c1.name, "\t\t\t ",c1.HP, "\t",c1.Mp,  "\t",c1.Atk,  "\t",c1.Lvl)
print(c2.name, "\t\t\t ",c2.HP, "\t",c2.Mp,  "\t",c2.Atk,  "\t",c2.Lvl)
print(c3.name, "\t\t\t ",c3.HP, "\t",c3.Mp,  "\t",c3.Atk,  "\t",c3.Lvl)
print(c4.name, "\t\t\t ",c4.HP, "\t",c4.Mp,  "\t",c4.Atk,  "\t",c4.Lvl)
print(c5.name, "\t\t\t ",c5.HP, "\t",c5.Mp,  "\t",c5.Atk,  "\t",c5.Lvl)