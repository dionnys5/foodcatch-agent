# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
import random

food = PVector(random.randint(1, 640), random.randint(1, 360))
catch = 0

def setup():
    global v
    size(640, 360)
    v = Vehicle(width / 2, height / 2)

def draw():
    background(51)
    textSize(20)
    text(catch, 10, 30);       
    fill(1)
    local_food = food
    # mouse = PVector(mouseX, mouseY)
    if dist(local_food.x, local_food.y, v.position.x, v.position.y) < 48:
        global food
        food = PVector(random.randint(1, 640),random.randint(1, 360))
        global catch
        catch += 1
        text(catch, 10, 30);
    # Draw an ellipse at the mouse position
    fill(127)
    stroke(200)
    strokeWeight(2)
    ellipse(local_food.x, local_food.y, 48, 48)

    # Call the appropriate steering behaviors for our agents
    v.arrive(local_food)
    v.update()
    v.display()
