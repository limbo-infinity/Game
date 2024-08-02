import pygame as py
import sys
import random

py.init()

WHITE = (255, 255, 255)

MAX_X = 1200
MAX_Y = 800


screen = py.display.set_mode((MAX_X, MAX_Y))


#General constants
RECT_MOVE = 0.5

#rectangle1 properties
rect1_x = 20
rect1_y = MAX_Y/2 - 50
rect1_width = 30
rect1_height = 130
rect1_speed = 10

#rectangle2 properties
rect2_x = MAX_X-50
rect2_y = MAX_Y/2 - 50
rect2_width = 30
rect2_height = 130
rect2_speed = 10


#circle properties
circle_x = MAX_X/2
circle_y = MAX_Y/2
# circle_vx = 0
# circle_vy = 0
circle_radius = 10
C_SPEED = MAX_Y/100 - 3
speed_mult = 1.15

clock = py.time.Clock()

random_int = random.randint(1, 2)
circle_vx = C_SPEED * (-1)**(random_int)
random_int = random.randint(1, 2)
circle_vy = (C_SPEED - 2) * (-1)**(random_int)

def colliding(rectangle_y, circle_vx, circle_y, circle_vy):
    top = circle_y - circle_radius
    bottom = circle_y + circle_radius
    if (((bottom > rectangle_y) and (bottom < rectangle_y + rect1_height)) or 
        ((top > rectangle_y) and (top < rectangle_y + rect1_height))):
        return ((circle_vx * (-speed_mult)), circle_vy)
    
    return (circle_vx, circle_vy)

while True:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    keys = py.key.get_pressed()
    if (rect1_y <= (MAX_Y - rect1_height)) and (rect1_y >= 0):
        if keys[py.K_w]:
            rect1_y -= rect1_speed
        if keys[py.K_s]:
            rect1_y += rect1_speed
    elif (rect1_y >= (MAX_Y - rect1_height)):
        rect1_y -= (RECT_MOVE)
    else:
        rect1_y += RECT_MOVE
        
    if (rect2_y <= (MAX_Y - rect2_height)) and (rect2_y >= 0):
        if keys[py.K_UP]:
            rect2_y -= rect2_speed
        if keys[py.K_DOWN]:
            rect2_y += rect2_speed
    elif (rect2_y >= (MAX_Y - rect2_height)):
        rect2_y -= (RECT_MOVE)
    else:
        rect2_y += RECT_MOVE
        
    # Fill the screen with a color (RGB)
    
    # Update circle position 
    if (circle_x - circle_radius < rect1_x + rect1_width):
        result = colliding(rect1_y, circle_vx, circle_y, circle_vy)
        circle_vx = result[0]
        circle_vy = result[1]
    elif (circle_x + circle_radius > rect2_x):
        result = colliding(rect2_y, circle_vx, circle_y, circle_vy)
        circle_vx = result[0]
        circle_vy = result[1]
        
    top = circle_y - circle_radius
    bottom = circle_y + circle_radius
    if (top < 0 or bottom > MAX_Y):
        circle_vy = circle_vy * (-1)
    
    circle_x += circle_vx
    circle_y += circle_vy
    
    screen.fill((0, 128, 255))
    
    # Draw a simple shape (rectangle)
    py.draw.rect(screen, WHITE, (rect1_x, rect1_y, rect1_width, rect1_height))
    py.draw.rect(screen, WHITE, (rect2_x, rect2_y, rect2_width, rect2_height))
    py.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)
    
    # Update the display
    py.display.flip()
    
    # Cap the frame rate at 60 frames per second
    clock.tick(60)