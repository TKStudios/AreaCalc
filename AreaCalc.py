
#the menu function:
def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),)
        print(") " + entry)

    return int(input(question)) - 1

# Class to define area and perimeter functions
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

# Class to define the Square subclass
class Square(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

# Menu list
items = ["Area (Square)","Area (Rectangle)","Area (Circle)","Perimeter (Square)","Perimeter (Rectangle)","Perimeter (Circle)","Exit"]

# Sets the initial value of the variable 'loop' to 1
loop = 1

# Main program that rotates through the menu and functions
# This program calculates the perimeter and area of a rectangle
while loop == 1:
    choice = menu(items,"Input Menu Choice (1,2,3,4,5,6 or 7)? ")
    if choice == 0:
        if choice == 0:
            print("You chose Area (Square)")
            print("")
            Square.x = float(input("Input Width? "))
            Square.area = (Square.x*Square.x)
            print("The Area of the Square is: ", Square.area)
            print("")
            
    elif choice == 1:
        if choice == 1:
            print("You chose Area (Rectangle)")
            print("")
            Shape.x = float(input("Input Width? "))
            Shape.y = float(input("Input Lenght? "))
            Shape.area = (Shape.x*Shape.y)
            print("The Area of the Rectangle is: ", Shape.area)
            print("")
            
            
    elif choice == 2:
        if choice == 2:
            print("You chose Area (Circle)")
            print("")
            pi = 3.14
            Shape.x = float(input("Input Radius? "))
            Shape.area = (pi*Shape.x*Shape.x)
            print("The area of the Circle is: ", Shape.area)
            print("")
            
    elif choice == 3:
        if choice == 3:
            print("You chose Perimeter (Square)")
            print("")
            Shape.x = float(input("Input Width? "))
            Shape.area = (4*Shape.x)
            print("The Perimeter of the Square is: ", Shape.area)
            print("")
            
    elif choice == 4:
        if choice == 4:
            print("You chose Perimeter (Rectangle)")
            print("")
            Shape.x = float(input("Input Width? "))
            Shape.y = float(input("Input Lenght? "))
            Shape.area = (2*Shape.x+2*Shape.y)
            print("The Perimieter of the Rectangle is: ", Shape.area)
            print("")
            
    elif choice == 5:
        if choice == 5:
            print("You chose Perimeter (Circle)")
            print("")
            pi = 3.14
            Shape.x = float(input("Input Radius? "))
            Shape.area = (2*pi*Shape.x)
            print("The Circumferance of the Circle is: ", Shape.area)
            print("")
            
        
    elif choice == 6:
        if choice == 6:
            exit("Goodbye")