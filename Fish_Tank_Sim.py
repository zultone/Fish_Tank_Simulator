from turtle import Turtle, Screen
import random
import time
import pygame
pygame.init()
pygame.mixer.init()
music = pygame.mixer.music.load('Music/fish_tank.mp3')
food_splash = pygame.mixer.Sound('Sounds/food_splash.mp3')
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)
screen = Screen()
screen.tracer(0)
screen.colormode(255)
screen.bgcolor(75,75,225)
screen.bgpic("background1.gif")
screen.title("Fishy Fish Tank")
# Blue Fish
screen.register_shape("blue_fish/blue_fish_right_1.gif")
screen.register_shape("blue_fish/blue_fish_right_2.gif")
screen.register_shape("blue_fish/blue_fish_right_3.gif")
blue_fish_right_list = ["blue_fish/blue_fish_right_1.gif",
                        "blue_fish/blue_fish_right_2.gif",
                        "blue_fish/blue_fish_right_3.gif"]

screen.register_shape("blue_fish/blue_fish_down_1.gif")
screen.register_shape("blue_fish/blue_fish_down_2.gif")
screen.register_shape("blue_fish/blue_fish_down_3.gif")
blue_fish_down_list = ["blue_fish/blue_fish_down_1.gif",
                       "blue_fish/blue_fish_down_2.gif",
                       "blue_fish/blue_fish_down_3.gif"]

screen.register_shape("blue_fish/blue_fish_left_1.gif")
screen.register_shape("blue_fish/blue_fish_left_2.gif")
screen.register_shape("blue_fish/blue_fish_left_3.gif")
blue_fish_left_list = ["blue_fish/blue_fish_left_1.gif",
                       "blue_fish/blue_fish_left_2.gif",
                       "blue_fish/blue_fish_left_3.gif"]

screen.register_shape("blue_fish/blue_fish_up_1.gif")
screen.register_shape("blue_fish/blue_fish_up_2.gif")
screen.register_shape("blue_fish/blue_fish_up_3.gif")
blue_fish_up_list = ["blue_fish/blue_fish_up_1.gif",
                     "blue_fish/blue_fish_up_2.gif",
                     "blue_fish/blue_fish_up_3.gif"] 
# Dark Fish
screen.register_shape("dark_fish/dark_fish_right_1.gif")
screen.register_shape("dark_fish/dark_fish_right_2.gif")
screen.register_shape("dark_fish/dark_fish_right_3.gif")
dark_fish_right_list = ["dark_fish/dark_fish_right_1.gif",
                        "dark_fish/dark_fish_right_2.gif",
                        "dark_fish/dark_fish_right_3.gif"]

screen.register_shape("dark_fish/dark_fish_down_1.gif")
screen.register_shape("dark_fish/dark_fish_down_2.gif")
screen.register_shape("dark_fish/dark_fish_down_3.gif")
dark_fish_down_list = ["dark_fish/dark_fish_down_1.gif",
                       "dark_fish/dark_fish_down_2.gif",
                       "dark_fish/dark_fish_down_3.gif"]

screen.register_shape("dark_fish/dark_fish_left_1.gif")
screen.register_shape("dark_fish/dark_fish_left_2.gif")
screen.register_shape("dark_fish/dark_fish_left_3.gif")
dark_fish_left_list = ["dark_fish/dark_fish_left_1.gif",
                       "dark_fish/dark_fish_left_2.gif",
                       "dark_fish/dark_fish_left_3.gif"]

screen.register_shape("dark_fish/dark_fish_up_1.gif")
screen.register_shape("dark_fish/dark_fish_up_2.gif")
screen.register_shape("dark_fish/dark_fish_up_3.gif")
dark_fish_up_list = ["dark_fish/dark_fish_up_1.gif",
                     "dark_fish/dark_fish_up_2.gif",
                     "dark_fish/dark_fish_up_3.gif"]

# Green Fish
screen.register_shape("green_fish/green_fish_right_1.gif")
screen.register_shape("green_fish/green_fish_right_2.gif")
screen.register_shape("green_fish/green_fish_right_3.gif")
green_fish_right_list = ["green_fish/green_fish_right_1.gif",
                         "green_fish/green_fish_right_2.gif",
                         "green_fish/green_fish_right_3.gif"]

screen.register_shape("green_fish/green_fish_down_1.gif")
screen.register_shape("green_fish/green_fish_down_2.gif")
screen.register_shape("green_fish/green_fish_down_3.gif")
green_fish_down_list = ["green_fish/green_fish_down_1.gif",
                        "green_fish/green_fish_down_2.gif",
                        "green_fish/green_fish_down_3.gif"]

screen.register_shape("green_fish/green_fish_left_1.gif")
screen.register_shape("green_fish/green_fish_left_2.gif")
screen.register_shape("green_fish/green_fish_left_3.gif")
green_fish_left_list = ["green_fish/green_fish_left_1.gif",
                        "green_fish/green_fish_left_2.gif",
                        "green_fish/green_fish_left_3.gif"]

screen.register_shape("green_fish/green_fish_up_1.gif")
screen.register_shape("green_fish/green_fish_up_2.gif")
screen.register_shape("green_fish/green_fish_up_3.gif")
green_fish_up_list = ["green_fish/green_fish_up_1.gif",
                      "green_fish/green_fish_up_2.gif",
                      "green_fish/green_fish_up_3.gif"]

# Grey Fish
screen.register_shape("grey_fish/grey_fish_right_1.gif")
screen.register_shape("grey_fish/grey_fish_right_2.gif")
screen.register_shape("grey_fish/grey_fish_right_3.gif")
grey_fish_right_list = ["grey_fish/grey_fish_right_1.gif",
                        "grey_fish/grey_fish_right_2.gif",
                        "grey_fish/grey_fish_right_3.gif"]

screen.register_shape("grey_fish/grey_fish_down_1.gif")
screen.register_shape("grey_fish/grey_fish_down_2.gif")
screen.register_shape("grey_fish/grey_fish_down_3.gif")
grey_fish_down_list = ["grey_fish/grey_fish_down_1.gif",
                       "grey_fish/grey_fish_down_2.gif",
                       "grey_fish/grey_fish_down_3.gif"]

screen.register_shape("grey_fish/grey_fish_left_1.gif")
screen.register_shape("grey_fish/grey_fish_left_2.gif")
screen.register_shape("grey_fish/grey_fish_left_3.gif")
grey_fish_left_list = ["grey_fish/grey_fish_left_1.gif",
                       "grey_fish/grey_fish_left_2.gif",
                       "grey_fish/grey_fish_left_3.gif"]

screen.register_shape("grey_fish/grey_fish_up_1.gif")
screen.register_shape("grey_fish/grey_fish_up_2.gif")
screen.register_shape("grey_fish/grey_fish_up_3.gif")
grey_fish_up_list = ["grey_fish/grey_fish_up_1.gif",
                     "grey_fish/grey_fish_up_2.gif",
                     "grey_fish/grey_fish_up_3.gif"]

# Lime Fish
screen.register_shape("lime_fish/lime_fish_right_1.gif")
screen.register_shape("lime_fish/lime_fish_right_2.gif")
screen.register_shape("lime_fish/lime_fish_right_3.gif")
lime_fish_right_list = ["lime_fish/lime_fish_right_1.gif",
                        "lime_fish/lime_fish_right_2.gif",
                        "lime_fish/lime_fish_right_3.gif"]

screen.register_shape("lime_fish/lime_fish_down_1.gif")
screen.register_shape("lime_fish/lime_fish_down_2.gif")
screen.register_shape("lime_fish/lime_fish_down_3.gif")
lime_fish_down_list = ["lime_fish/lime_fish_down_1.gif",
                       "lime_fish/lime_fish_down_2.gif",
                       "lime_fish/lime_fish_down_3.gif"]

screen.register_shape("lime_fish/lime_fish_left_1.gif")
screen.register_shape("lime_fish/lime_fish_left_2.gif")
screen.register_shape("lime_fish/lime_fish_left_3.gif")
lime_fish_left_list = ["lime_fish/lime_fish_left_1.gif",
                       "lime_fish/lime_fish_left_2.gif",
                       "lime_fish/lime_fish_left_3.gif"]

screen.register_shape("lime_fish/lime_fish_up_1.gif")
screen.register_shape("lime_fish/lime_fish_up_2.gif")
screen.register_shape("lime_fish/lime_fish_up_3.gif")
lime_fish_up_list = ["lime_fish/lime_fish_up_1.gif",
                     "lime_fish/lime_fish_up_2.gif",
                     "lime_fish/lime_fish_up_3.gif"]

# Red Fish
screen.register_shape("red_fish/red_fish_right_1.gif")
screen.register_shape("red_fish/red_fish_right_2.gif")
screen.register_shape("red_fish/red_fish_right_3.gif")
red_fish_right_list = ["red_fish/red_fish_right_1.gif",
                      "red_fish/red_fish_right_2.gif",
                      "red_fish/red_fish_right_3.gif"]

screen.register_shape("red_fish/red_fish_down_1.gif")
screen.register_shape("red_fish/red_fish_down_2.gif")
screen.register_shape("red_fish/red_fish_down_3.gif")
red_fish_down_list = ["red_fish/red_fish_down_1.gif",
                      "red_fish/red_fish_down_2.gif",
                      "red_fish/red_fish_down_3.gif"]

screen.register_shape("red_fish/red_fish_left_1.gif")
screen.register_shape("red_fish/red_fish_left_2.gif")
screen.register_shape("red_fish/red_fish_left_3.gif")
red_fish_left_list = ["red_fish/red_fish_left_1.gif",
                      "red_fish/red_fish_left_2.gif",
                      "red_fish/red_fish_left_3.gif"]

screen.register_shape("red_fish/red_fish_up_1.gif")
screen.register_shape("red_fish/red_fish_up_2.gif")
screen.register_shape("red_fish/red_fish_up_3.gif")
red_fish_up_list = ["red_fish/red_fish_up_1.gif",
                    "red_fish/red_fish_up_2.gif",
                    "red_fish/red_fish_up_3.gif"]

# Tan Fish
screen.register_shape("tan_fish/tan_fish_right_1.gif")
screen.register_shape("tan_fish/tan_fish_right_2.gif")
screen.register_shape("tan_fish/tan_fish_right_3.gif")
tan_fish_right_list = ["tan_fish/tan_fish_right_1.gif",
                       "tan_fish/tan_fish_right_2.gif",
                       "tan_fish/tan_fish_right_3.gif"]

screen.register_shape("tan_fish/tan_fish_down_1.gif")
screen.register_shape("tan_fish/tan_fish_down_2.gif")
screen.register_shape("tan_fish/tan_fish_down_3.gif")
tan_fish_down_list = ["tan_fish/tan_fish_down_1.gif",
                      "tan_fish/tan_fish_down_2.gif",
                      "tan_fish/tan_fish_down_3.gif"]

screen.register_shape("tan_fish/tan_fish_left_1.gif")
screen.register_shape("tan_fish/tan_fish_left_2.gif")
screen.register_shape("tan_fish/tan_fish_left_3.gif")
tan_fish_left_list = ["tan_fish/tan_fish_left_1.gif",
                      "tan_fish/tan_fish_left_2.gif",
                      "tan_fish/tan_fish_left_3.gif"]

screen.register_shape("tan_fish/tan_fish_up_1.gif")
screen.register_shape("tan_fish/tan_fish_up_2.gif")
screen.register_shape("tan_fish/tan_fish_up_3.gif")
tan_fish_up_list = ["tan_fish/tan_fish_up_1.gif",
                    "tan_fish/tan_fish_up_2.gif",
                    "tan_fish/tan_fish_up_3.gif"]

# White Fish
screen.register_shape("white_fish/white_fish_right_1.gif")
screen.register_shape("white_fish/white_fish_right_2.gif")
screen.register_shape("white_fish/white_fish_right_3.gif")
white_fish_right_list = ["white_fish/white_fish_right_1.gif",
                         "white_fish/white_fish_right_2.gif",
                         "white_fish/white_fish_right_3.gif"]

screen.register_shape("white_fish/white_fish_down_1.gif")
screen.register_shape("white_fish/white_fish_down_2.gif")
screen.register_shape("white_fish/white_fish_down_3.gif")
white_fish_down_list = ["white_fish/white_fish_down_1.gif",
                        "white_fish/white_fish_down_2.gif",
                        "white_fish/white_fish_down_3.gif"]

screen.register_shape("white_fish/white_fish_left_1.gif")
screen.register_shape("white_fish/white_fish_left_2.gif")
screen.register_shape("white_fish/white_fish_left_3.gif")
white_fish_left_list = ["white_fish/white_fish_left_1.gif",
                        "white_fish/white_fish_left_2.gif",
                        "white_fish/white_fish_left_3.gif"]

screen.register_shape("white_fish/white_fish_up_1.gif")
screen.register_shape("white_fish/white_fish_up_2.gif")
screen.register_shape("white_fish/white_fish_up_3.gif")
white_fish_up_list = ["white_fish/white_fish_up_1.gif",
                      "white_fish/white_fish_up_2.gif",
                      "white_fish/white_fish_up_3.gif"]

# Player fish
screen.register_shape("Player/player_up_1.gif")
screen.register_shape("Player/player_up_2.gif")
screen.register_shape("Player/player_up_3.gif")
player_fish_up_list = ["Player/player_up_1.gif",
                       "Player/player_up_2.gif",
                       "Player/player_up_3.gif"]

screen.register_shape("Player/player_down_1.gif")
screen.register_shape("Player/player_down_2.gif")
screen.register_shape("Player/player_down_3.gif")
player_fish_down_list = ["Player/player_down_1.gif",
                         "Player/player_down_2.gif",
                         "Player/player_down_3.gif"]

screen.register_shape("Player/player_left_1.gif")
screen.register_shape("Player/player_left_2.gif")
screen.register_shape("Player/player_left_3.gif")
player_fish_left_list = ["Player/player_left_1.gif",
                         "Player/player_left_2.gif",
                         "Player/player_left_3.gif"]

screen.register_shape("Player/player_right_1.gif")
screen.register_shape("Player/player_right_2.gif")
screen.register_shape("Player/player_right_3.gif")
player_fish_right_list = ["Player/player_right_1.gif",
                          "Player/player_right_2.gif",
                          "Player/player_right_3.gif"]
# Bubble Sprites
screen.register_shape("Sprites/Bubble_1.gif")
screen.register_shape("Sprites/Bubble_2.gif")
screen.register_shape("Sprites/Bubble_3.gif")
sprite_bubble_list = ["Sprites/Bubble_1.gif",
                      "Sprites/Bubble_2.gif",
                      "Sprites/Bubble_3.gif"]
# Chest Sprites
screen.register_shape("Sprites/chest_1.gif")
screen.register_shape("Sprites/chest_2.gif")
screen.register_shape("Sprites/chest_3.gif")
sprite_chest_list = ["Sprites/chest_1.gif",
                     "Sprites/chest_2.gif",
                     "Sprites/chest_3.gif"]

################################################################################################
# VARIABLES

DELAY = .07
FEEDING = False
DIR_LIST = ["left","right","up","down"]
FOOD_LIST = []
BUBBLE_LIST = []
choiceList = [1,-1]


"""
Add bubbles that come  up from bottom of screen

Add aquarium sounds
"""


#################################################################################################
class Writer(Turtle):
    def __init__(self,x,y):
        super().__init__(shape='square', visible=False)
        self.pu()
        self.x = x
        self.y = y
        self.goto(x,y)
        self.style = ('Arial', 8, 'normal')
        

class Chest(Turtle):
    def __init__(self):
        super().__init__(shape='square', visible=True)
        self.pu()
        self.goto(-300,-300)
        self.open = False
        self.count = 0
        self.shape("Sprites/chest_1.gif")

    def animate_chest(self):
        if self.count < 3:
            self.shape(sprite_chest_list[self.count])
            self.count += 1
        else:
            self.count = 0
            
        screen.ontimer(self.animate_chest,900)
        
class Bubbles(Turtle):
    def __init__(self):
        super().__init__(shape="Sprites/Bubble_1.gif", visible=True)    
        self.pu()
        self.goto(random.randrange(-325,-275), -300)
        self.gravity = random.uniform(.1,3)
        self.vel_count = 0
        self.flip = False
    def move(self):
        if not self.flip:
            self.vel_count += .5
            if self.vel_count > random.randrange(1,3,1):
                self.flip = True
        if self.flip:
            self.vel_count -= .5
            if self.vel_count < random.randrange(1,3,1)*-1:
                self.flip = False
        if self.ycor() > 300:
            self.ht()
            self.goto(-300,-300)
            self.st()
        self.goto(self.xcor()+self.vel_count,self.ycor() + self.gravity)

        screen.ontimer(self.move, 150)
        
class Hunger_bar(Turtle):
    def __init__(self, color):
        super().__init__(shape='square', visible=True)
        self.pu()
        self.color(color) 
        self.rate = .02
        self.bar_length = 8
        self.shapesize(.5,self.bar_length)
        self.goto(550,330)
        self.hungry = True
        self.running = True
        self.count = 0

    def shrink_bar(self):
        global DELAY
        if self.running:
            if FOOD_LIST:
                self.hungry = False
            else:
                self.hungry = True
                
            if self.hungry:
                if self.bar_length > .04:
                    self.bar_length -= self.rate
                    self.shapesize(.5,self.bar_length)
                if self.bar_length < .05:
                    if DELAY < 5:
                        DELAY += .002
            elif not self.hungry:
                self.bar_length = 8
                self.shapesize(.5,self.bar_length)
                DELAY = .07

        
        
class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle', visible=False)
        self.pu()
        self.st()
        self.shapesize(.3)
        self.goto(random.randrange(-450,450), random.randrange(300,350,1))
        self.gravity = random.uniform(.1,1.5)
        self.vel_count = 0
        self.flip = False
        self.color(random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1))
        
    def move(self):
        if not self.flip:
            self.vel_count += .5
            if self.vel_count > random.randrange(1,3,1):
                self.flip = True
        if self.flip:
            self.vel_count -= .5
            if self.vel_count < random.randrange(1,3,1)*-1:
                self.flip = False
        if self.ycor() < -300:
            self.ht()
        self.goto(self.xcor(),self.ycor() - self.gravity)
##        self.goto(self.xcor()+self.vel_count,self.ycor() - self.gravity)
        # Make food go side to side
        # Make food drop slowly as it wiggles down
        # Fish will follow food
        # Make food following function
        # Food will be fed when user hits space,
        # it will be eaten when fish get close enough to the food
        

class Fish(Turtle):
    def __init__(self):
        super().__init__(shape='square', visible=False)
        self.st()
        self.pu()
        self.shape()
        self.goto(random.randrange(-450,450),random.randrange(-300,300))
        self.vel_choice = random.choice(choiceList)
        self.boost = 0
        self.velocity_x = self.boost + random.randrange(2,5,1) * self.vel_choice
        self.velocity_y = self.boost + random.uniform(.1,.3) * self.vel_choice
        self.count = 0
        self.direction_change = 0
        self.state = False
        
##    def move_fish():
##        self.goto(self.xcor()+self.velocity_x, self.ycor()+self.velocity_y())
# Right fish:
# Blue, dark, green, grey

# Left fish:
# Lime, red, tan, white
class Player(Fish):
    def __init__(self):
        super().__init__()
        self.shape("Player/player_right_1.gif")
        self.direction = "right"
        self.auto = False
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 5.5
        self.shape(player_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -5.5
        self.shape(player_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        self.velocity_x = -5.5 - self.boost
        self.counter()
        self.shape(player_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        self.velocity_x = 5.5 + self.boost
        self.counter()
        self.shape(player_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
        
class Blue_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("blue_fish/blue_fish_right_1.gif")
        self.direction = "right"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(blue_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(blue_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(blue_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(blue_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())


class Dark_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("dark_fish/dark_fish_right_1.gif")
        self.direction = "right"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(dark_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(dark_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(dark_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(dark_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())

class Green_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("green_fish/green_fish_right_1.gif")
        self.direction = "right"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(green_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(green_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(green_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(green_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
        
class Grey_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("grey_fish/grey_fish_right_1.gif")
        self.direction = "right"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(grey_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(grey_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(grey_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(grey_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
        
class Lime_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("lime_fish/lime_fish_left_1.gif")
        self.direction = "left"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(lime_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(lime_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(lime_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(lime_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
        
class Red_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("red_fish/red_fish_left_1.gif")
        self.direction = "left"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(red_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(red_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(red_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(red_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
        
class Tan_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("tan_fish/tan_fish_left_1.gif")
        self.direction = "left"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(tan_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(tan_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(tan_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(tan_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())

class White_Fish(Fish):
    def __init__(self):
        super().__init__()
        self.shape("white_fish/white_fish_left_1.gif")
        self.direction = "left"
        # Directions - left, right, up, down, follow
        # Follow - when 'feeding' fish, they will follow food
    def counter(self):
        if self.count <= 2:
            self.count += 1
        if self.count > 2:
            self.count = 0        
        
    def go_up(self):
        self.counter()
        self.velocity_y = 4
        self.shape(white_fish_up_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_down(self):
        self.counter()
        self.velocity_y = -4
        self.shape(white_fish_down_list[self.count])
        self.goto(self.xcor(), self.ycor()+self.velocity_y)
    def go_left(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(white_fish_left_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
    def go_right(self):
        if self.velocity_x < 0:
            self.velocity_x = self.velocity_x * -1
        self.counter()
        self.shape(white_fish_right_list[self.count])
        self.goto(self.xcor()+self.velocity_x, self.ycor())
        
# Right fish:
# Blue, dark, green, grey

# Left fish:
# Lime, red, tan, white

#Initialize fishies
blue_fish_1 = Blue_Fish()
dark_fish_1 = Dark_Fish()
green_fish_1 = Green_Fish()
grey_fish_1 = Grey_Fish()
lime_fish_1 = Lime_Fish()
red_fish_1 = Red_Fish()
tan_fish_1 = Tan_Fish()
white_fish_1 = White_Fish()

PLAYER = Player()
chest = Chest()
chest.animate_chest()
for i in range(15):
    BUBBLE_LIST.append(Bubbles())

for i in BUBBLE_LIST:
    i.move()
fish_list = [blue_fish_1,dark_fish_1,green_fish_1,grey_fish_1,lime_fish_1,red_fish_1,tan_fish_1,white_fish_1]

FOLLOW_LIST = []
        
def feed():
    if not FOOD_LIST:
        food_splash.play()
        for i in range(15):
            FOOD_LIST.append(Food())
            
def follow_food():
    for index, fish in enumerate(fish_list):
        if FOOD_LIST:

            
            try:
               
                if fish.xcor() > FOOD_LIST[index].ycor():  
                    if fish.xcor() > FOOD_LIST[index].xcor():

                        if int(fish.xcor()) not in range(int(FOOD_LIST[index].xcor())-15,int(FOOD_LIST[index].xcor())+15):
                        
                            if fish.direction != "right":
                                fish.direction = "left"
                                fish.state = True
                        else:
                            if fish.direction != "left":
                                fish.direction = "right"
                                fish.state = True
                

                if not fish.state:
                    if fish.ycor() > FOOD_LIST[index].ycor():
                        if fish.direction != "up":
                            fish.direction = "down"
                    else:
                        if fish.direction != "down":
                            fish.direction = "up"
                fish.state = False
                
            except:
                pass

                    
                
                    
                
        
        
        
            
def follow_food_():
    if len(FOOD_LIST) >= len(fish_list):
        for index, fish in enumerate(fish_list):
            fish.boost = random.randrange(4,10,1)
            PLAYER.boost = 2
            if fish.distance(FOOD_LIST[index]) > 30:
                if fish.ycor() not in range(int(FOOD_LIST[index].ycor())-15,int(FOOD_LIST[index].ycor())+15):
                    if FOOD_LIST[index].ycor() < fish.ycor() and not fish.state:
                        
                        fish.direction = "down"
                        fish.state = True
                            
                                            
                    if FOOD_LIST[index].ycor() > fish.ycor() and not fish.state:
                        
                        fish.direction = "up"
                        fish.state = True
                
            
                if fish.xcor() not in range(int(FOOD_LIST[index].xcor())-15,int(FOOD_LIST[index].xcor())+15):    
                    if FOOD_LIST[index].xcor() < fish.xcor() and not fish.state:
                        
                        fish.direction = "left"
                        fish.state = True
                            
                        
                        
                    if FOOD_LIST[index].xcor() > fish.xcor() and not fish.state:
                        
                        fish.direction = "right"
                        fish.state = True
                    
            else:
                fish.setheading(fish.towards(FOOD_LIST[index].pos()))
                fish.forward(5)
                
            fish.state = False                    
    else:
        if FOOD_LIST:
            for food in FOOD_LIST:
                for fish in fish_list:
                    if fish.distance(food) > 30:
                        if fish.ycor() not in range(int(food.ycor())-15,int(food.ycor())+15): 
                            if food.ycor() < fish.ycor() and not fish.state:
                                if fish.direction != "up":
                                    fish.direction = "down"
                                    fish.state = True
                                    
                                
                                
                            if food.ycor() > fish.ycor() and not fish.state:
                                if fish.direction != "down":
                                    fish.direction = "up"
                                    fish.state = True
                                
                        if fish.xcor() not in range(int(food.xcor())-15,int(food.xcor())+15):        
                            if food.xcor() < fish.xcor() and not fish.state:
                                if fish.direction != "right":
                                    fish.direction = "left"
                                    fish.state = True
                                    
                                
                                
                            if food.xcor() > fish.xcor() and not fish.state:
                                if fish.direction != "left":
                                    fish.direction = "right"
                                    fish.state = True
                            
                else:
                    fish.setheading(fish.towards(food.pos()))
                    fish.forward(5)
                    fish.state = False
                    
    if not FOOD_LIST:
        for fish in fish_list:
            fish.boost = 0
            PLAYER.boost = 0
            
def check_collisions():
    for food in FOOD_LIST:
        for fish in fish_list:
            if fish.distance(food) < 15:
                food.goto(food.xcor(), -600)
                food.ht()
                FOOD_LIST.remove(food)
            if PLAYER.distance(food) < 30:
                food.goto(food.xcor(), -600)
                food.ht()
                FOOD_LIST.remove(food)
                
def move_player():
    PLAYER.direction_change += 1
    if PLAYER.xcor() > 550:
        PLAYER.direction = "left"
    elif PLAYER.xcor() < -550:
        PLAYER.direction = "right"
    if PLAYER.ycor() > 300:
        PLAYER.direction = "down"
    elif PLAYER.ycor() < -300:
        PLAYER.direction = "up"
        
    if PLAYER.direction == "left":
        PLAYER.go_left()
    elif PLAYER.direction == "right":
        PLAYER.go_right()
    elif PLAYER.direction == "up":
        PLAYER.go_up()
    elif PLAYER.direction == "down":
        PLAYER.go_down()
        
    if PLAYER.auto:
        if PLAYER.direction_change == random.randrange(35,75,1):
            PLAYER.direction_change = 0
            while True:
                direct = random.choice(DIR_LIST)
                if PLAYER.direction != direct:
                    PLAYER.direction = direct
                    break
        elif PLAYER.direction_change > 75:
            PLAYER.direction_change = 0
            while True:
                direct = random.choice(DIR_LIST)
                if PLAYER.direction != direct:
                    PLAYER.direction = direct
                    break
def move_fish():
    
    for fish in fish_list:
        fish.direction_change += 1
        if fish.xcor() > 550:
            fish.direction = "left"
        elif fish.xcor() < -550:
            fish.direction = "right"
        if fish.ycor() > 335:
            fish.direction = "down"
        elif fish.ycor() < -300:
            fish.direction = "up"

        if fish.direction == "left":
            fish.go_left()
        elif fish.direction == "right":
            fish.go_right()
        elif fish.direction == "up":
            fish.go_up()
        elif fish.direction == "down":
            fish.go_down()

        if len(FOOD_LIST) < 1:
            if fish.direction_change == random.randrange(35,75,1):
                fish.direction_change = 0
                while True:
                    direct = random.choice(DIR_LIST)
                    if fish.direction != direct:
                        fish.direction = direct
                        break
            elif fish.direction_change > 75:
                fish.direction_change = 0
                while True:
                    direct = random.choice(DIR_LIST)
                    if fish.direction != direct:
                        fish.direction = direct
                        break
            
def move_food():
    if FOOD_LIST:
        for food in FOOD_LIST:
            food.move()
            if food.ycor() < -325:
                FOOD_LIST.remove(food)
                
def player_up():
    PLAYER.direction = "up"
def player_down():
    PLAYER.direction = "down"
def player_right():
    PLAYER.direction = "right"
def player_left():
    PLAYER.direction = "left"
def hunger_off():
    if green_bar.count == 0:
        green_bar.running = True
        green_bar.count += 1
        hunger_writer.clear()
        hunger_writer.write("Hunger: ON\n'o' to toggle", move=False, align='left', font=hunger_writer.style)
    else:
        hunger_writer.clear()
        hunger_writer.write("Hunger: OFF\n'o' to toggle", move=False, align='left', font=hunger_writer.style)
        green_bar.running = False
        green_bar.count = 0
def auto_play():
    if PLAYER.auto:
        PLAYER.auto = False
        autopilot_writer.clear()
        autopilot_writer.write("Auto: OFF\n'Enter' to toggle", move=False, align='left', font=autopilot_writer.style)
    else:
        PLAYER.auto = True
        autopilot_writer.clear()
        autopilot_writer.write("Auto: ON\n'Enter' to toggle", move=False, align='left', font=autopilot_writer.style)
    print(PLAYER.auto)
    
red_bar = Hunger_bar("red")
green_bar = Hunger_bar("green")
hunger_writer = Writer(550,280)
autopilot_writer = Writer(550,250)
feeding_writer = Writer(550,230)
hunger_writer.write("Hunger: ON\n'o' to toggle", move=False, align='left', font=hunger_writer.style)
autopilot_writer.write("Auto: OFF\n'Enter' to toggle", move=False, align='left', font=autopilot_writer.style)
feeding_writer.write("SPACE to feed fish", move=False, align='left', font=autopilot_writer.style)
##write(line, move=False, align='center', font=)

while True:
    green_bar.shrink_bar()
    time.sleep(DELAY)
    move_fish()
    move_food()
    follow_food()
    check_collisions()
    move_player()
    screen.onkey(player_up, "Up")
    screen.onkey(player_down, "Down")
    screen.onkey(player_right, "Right")
    screen.onkey(player_left, "Left")
    screen.onkey(hunger_off, "o")
    screen.onkey(auto_play, "Return")
    screen.onkey(feed, "space")
    screen.listen()
    screen.update()











