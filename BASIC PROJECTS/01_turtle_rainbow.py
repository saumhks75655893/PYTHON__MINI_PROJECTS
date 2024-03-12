import turtle

# Create a turtle object
rainbow = turtle.Turtle()
rainbow.speed(10)  # Set the drawing speed

# Set starting position
rainbow.penup()
rainbow.goto(-300, -200)
rainbow.pendown()

# Rainbow colors
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# Rainbow radius
radius = 300

# Draw the rainbow
for color in colors:
    rainbow.penup()
    rainbow.color(color)
    rainbow.pendown()
    rainbow.begin_fill()
    rainbow.circle(radius)
    rainbow.penup()
    rainbow.left(90)
    rainbow.forward(20)
    rainbow.left(90)
    rainbow.pendown()
    rainbow.end_fill()
    radius -= 20

# Hide the turtle
rainbow.hideturtle()

# Keep the window open
turtle.done()
