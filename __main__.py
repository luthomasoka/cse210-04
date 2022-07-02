import os
import random

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.rock import Rock
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_GEMS = 20
DEFAULT_ROCKS = 15


def main():
    
    # create the cast
    cast = Cast()

    # create score
    score = Actor()
    score.set_text("Score: 0")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(10, 0))
    cast.add_actor("score", score)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 15)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the GEMS 
    for _ in range(DEFAULT_GEMS):
        text = '*'        
    
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        x = 0
        y = random.randint(1, 5)
        velocity = Point(x, y)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gems = Gem()
        gems.set_text(text)
        gems.set_font_size(FONT_SIZE)
        gems.set_color(color)
        gems.set_velocity(velocity)
        gems.set_position(position)
        cast.add_actor("gems", gems)

     # create the ROCKS 
    for _ in range(DEFAULT_ROCKS):
        text = 'o'        
        
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        x = 0
        y = random.randint(1, 5)
        velocity = Point(x, y)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        rocks = Rock()
        rocks.set_text(text)
        rocks.set_font_size(FONT_SIZE)
        rocks.set_color(color)
        rocks.set_velocity(velocity)
        rocks.set_position(position)
        cast.add_actor("rocks", rocks)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()