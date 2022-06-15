def square_foot():
    length = float(input("How long is the room you are trying to measure? "))
    width = float(input("How wide is the room you are trying to measure?"))
    area = length * width
    print(area)
    
def circumference():
    PI = 3.1415926
    radius = float(input("What is the radius of the circle that you want the circumference from? "))
    c = 2 * PI * radius
    print(c)