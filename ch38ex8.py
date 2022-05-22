def display_menu:
    print("1.Enter radius")
    print("2.Display radius")
    print("3.Display diameter")
    print("4.Display area")
    print("5.Display perimeter")
    print("6.Exit")

class Circle:
    radius = None
    def __init__(radius):
        self.radius = radius
    @property
    def radius(self):
        if radius == None:
            print("Error: Radius has not been entered yet.")
        else:
            return self.radius
    
