# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle()
bob.turtlesize(2)

# Step 3: Move in the direction Bob's facing for 50 pixels
for a in range(4):
  bob.forward(50)
  bob.left(90)

# Step 4: We're done!
turtle.done()