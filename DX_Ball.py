'''
Author: Ruihao Ni
EN.640.635 Software Carpentry
Final Project DX-Ball Game

This is a program of DX-Ball game based on the pygame module
used the paddle to hit the ball and control the direction
and finally eliminate all the bricks.
There are three levels of game: Casual, Normal and Advanced
The casual mode has longer paddle and larger, slower ball
The advanced mode has a shorter paddle and smaller, faster ball.
You can control the ball by using different part of paddle to
receive it.
'''

import pygame
from pygame.locals import *
import sys
import time
import math


class GameWindow():
    '''
    The game window class, set up the size of the window and
    with title and background color.
    '''

    def __init__(self, *args, **kw):
        # set the size of the window
        self.window_width = 600
        self.window_height = 500
        # print the game window
        self.game_window = pygame.display.set_mode(
            (self.window_width, self.window_height))
        # set the title
        pygame.display.set_caption("DX-Ball")
        # set the color of game window
        self.window_color = (40, 40, 40)

    def bgcolor(self):
        # set the background color
        self.game_window.fill(self.window_color)


class Ball1():
    '''
    create the ball object for the casual (easy) level
    '''

    def __init__(self, *args, **kw):

        # set the radius, color and speed parameter
        self.ball_color = (192, 192, 192)
        self.move_x = 3
        self.move_y = 3
        self.radius = 14
        self.speed = 4

    def ballready(self):
        # set the initial position of the ball
        # x: the same as where the mouse is (middle of the paddle)
        # y: right above the stick
        self.ball_x = self.mouse_x
        self.ball_y = self.window_height - self.paddle_height - self.radius
        pygame.draw.circle(self.game_window, self.ball_color,
                           (self.ball_x, self.ball_y), self.radius)

    def ballmove(self):
        # print the ball in the next frame
        pygame.draw.circle(self.game_window, self.ball_color,
                           (self.ball_x, self.ball_y), self.radius)
        # move the ball to the next position
        self.ball_x += self.move_x
        self.ball_y -= self.move_y
        # load the ball-window and ball-paddle collision function
        self.ball_window()
        self.ball_paddle()

        # if failed to collect the ball, the ball will be lower than
        # the paddle, which means losing the game.
        if self.ball_y > 520:
            self.game_window.blit(self.start, (30, 340))
            self.game_window.blit(self.gameover, (100, 230))
            self.game_window.blit(self.indicator, (30, 400))
            self.over_sign = 1


class Ball2():
    '''
    Create the ball object for the normal(Medium) level
    '''

    def __init__(self, *args, **kw):
        # set the radius, color and speed parameter
        # The ball is smaller and faster
        self.ball_color = (192, 192, 192)
        self.move_x = 5
        self.move_y = 5
        self.radius = 12
        self.speed = 7

    def ballready(self):
        self.ball_x = self.mouse_x
        self.ball_y = self.window_height - self.paddle_height - self.radius
        pygame.draw.circle(self.game_window, self.ball_color,
                           (self.ball_x, self.ball_y), self.radius)

    def ballmove(self):
        pygame.draw.circle(self.game_window, self.ball_color,
                           (self.ball_x, self.ball_y), self.radius)
        self.ball_x += self.move_x
        self.ball_y -= self.move_y
        self.ball_window()
        self.ball_paddle()
        if self.ball_y > 520:
            self.game_window.blit(self.start, (30, 340))
            self.game_window.blit(self.gameover, (100, 230))
            self.game_window.blit(self.indicator, (30, 400))
            self.over_sign = 1


class Ball3():
    # Create the ball object for the advanced(Hard) level

    def __init__(self, *args, **kw):
        # set the radius, color and speed parameter
        # The ball is smallest and fastest
        self.ball_color = (192, 192, 192)
        self.move_x = 7
        self.move_y = 7
        self.radius = 10
        self.speed = 10

    def ballready(self):
        self.ball_x = self.mouse_x
        self.ball_y = self.window_height - self.paddle_height - self.radius
        pygame.draw.circle(self.game_window, self.ball_color,
                           (self.ball_x, self.ball_y), self.radius)

    def ballmove(self):

        pygame.draw.circle(self.game_window, self.ball_color,
                           (self.ball_x, self.ball_y), self.radius)
        self.ball_x += self.move_x
        self.ball_y -= self.move_y
        self.ball_window()
        self.ball_paddle()
        if self.ball_y > 520:
            self.game_window.blit(self.start, (30, 340))
            self.game_window.blit(self.gameover, (100, 230))
            self.game_window.blit(self.indicator, (30, 400))
            self.over_sign = 1


class Paddle1():
    '''Create the paddle object for casual level'''

    def __init__(self, *args, **kw):
        # set the color and size of the paddle
        # the casual level has the longest paddle
        self.paddle_width = 130
        self.paddle_height = 10
        self.paddle_color = (255, 0, 0)

    def paddle_move(self):
        # obtain mouse position parameter
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        # draw the rack and set the boundary
        # if the mouse goes near the left and right boundary, fix the
        # left or right side of the paddle on the window boundary
        if self.mouse_x >= self.window_width - self.paddle_width // 2:
            self.mouse_x = self.window_width - self.paddle_width // 2
        if self.mouse_x <= self.paddle_width // 2:
            self.mouse_x = self.paddle_width // 2

        pygame.draw.rect(self.game_window, self.paddle_color, ((self.mouse_x - self.paddle_width // 2),
                                                               (self.window_height - self.paddle_height), self.paddle_width, self.paddle_height))


class Paddle2():
    # Create the paddle object for normal level

    def __init__(self, *args, **kw):
        # the casual level has the shorter paddle
        self.paddle_width = 90
        self.paddle_height = 10
        self.paddle_color = (255, 0, 0)

    def paddle_move(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if self.mouse_x >= self.window_width - self.paddle_width // 2:
            self.mouse_x = self.window_width - self.paddle_width // 2
        if self.mouse_x <= self.paddle_width // 2:
            self.mouse_x = self.paddle_width // 2
        pygame.draw.rect(self.game_window, self.paddle_color, ((self.mouse_x - self.paddle_width // 2),
                                                               (self.window_height - self.paddle_height), self.paddle_width, self.paddle_height))


class Paddle3():
    # Create the paddle object for advanced level

    def __init__(self, *args, **kw):
        # the casual level has the shortest paddle
        self.paddle_color = (255, 0, 0)
        self.paddle_width = 50
        self.paddle_height = 10

    def paddle_move(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if self.mouse_x >= self.window_width - self.paddle_width // 2:
            self.mouse_x = self.window_width - self.paddle_width // 2
        if self.mouse_x <= self.paddle_width // 2:
            self.mouse_x = self.paddle_width // 2
        pygame.draw.rect(self.game_window, self.paddle_color, ((self.mouse_x - self.paddle_width // 2),
                                                               (self.window_height - self.paddle_height), self.paddle_width, self.paddle_height))


class Brick():
    def __init__(self, *args, **kw):
        # set the color, arrangement and size of the brick
        self.brick_color = (251, 233, 88)
        self.brick_list = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [
            1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
        self.brick_width = 80
        self.brick_height = 20

    def brickarrange(self):
        # show the brick by the list, if the brick is 1, show it.
        for i in range(7):
            for j in range(7):
                self.brick_x = j * (self.brick_width + 6) + 2
                self.brick_y = i * (self.brick_height + 10) + 20
                if self.brick_list[i][j] == 1:
                    pygame.draw.rect(self.game_window, self.brick_color, (
                        self.brick_x, self.brick_y, self.brick_width, self.brick_height))

                    # use the collision and relection function
                    self.ball_brick()
                    if self.distanceb < self.radius:
                        self.brick_list[i][j] = 0
                        self.score += 10
        # set the condition of victory, if all the brick are broken
        if self.brick_list == [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]:
            self.game_window.blit(self.win, (100, 230))
            self.game_window.blit(self.start, (30, 340))
            self.game_window.blit(self.indicator, (30, 400))
            self.win_sign = 1


class Collision():
    '''
    This is a collision class, which used to tackle with the collision and
    reflection problem. It defines how does the ball interact with the
    1) window boundary 2) paddle 3) brick by 1)collision 2) reflection
    reference: https://blog.csdn.net/momobaba2018/article/details/82823532
    '''

    # ball-window boundary:
    # The collision condition is: 1)left boundary: x=radius
    # 2)upper boundary: y=radius 3)right boundary: x=width-radius
    # Reflection: mirror reflection: vx=-vx or vy=-vy
    def ball_window(self):
        if self.ball_x <= self.radius or self.ball_x >= (self.window_width - self.radius):
            self.move_x = -self.move_x
        if self.ball_y <= self.radius:
            self.move_y = -self.move_y

    # ball-paddle:

    def ball_paddle(self):
        # define the collision sign
        self.collision_sign_x = 0
        self.collision_sign_y = 0

        # find the closest point on the paddle to the ball.

        if self.ball_x < (self.mouse_x - self.paddle_width // 2):
            # The ball is on the left side of the paddle
            self.closestpoint_x = self.mouse_x - self.paddle_width // 2
            self.collision_sign_x = 1
        elif self.ball_x > (self.mouse_x + self.paddle_width // 2):
            # The ball is on the right side of the paddle
            self.closestpoint_x = self.mouse_x + self.paddle_width // 2
            self.collision_sign_x = 2
        else:
            # the ball is above the paddle
            self.closestpoint_x = self.ball_x
            self.collision_sign_x = 3

        if self.ball_y < (self.window_height - self.paddle_height):
            # The ball center is above the upper line of the paddle
            self.closestpoint_y = (self.window_height - self.paddle_height)
            self.collision_sign_y = 1
        elif self.ball_y > self.window_height:
            # The ball center is under the upper line of the paddle
            self.closestpoint_y = self.window_height
            self.collision_sign_y = 2
        else:
            # the ball center is on the left or right side of the paddle
            self.closestpoint_y = self.ball_y
            self.collision_sign_y = 3

        # define the distance of the ball center and the brick edge
        self.distance = math.sqrt(
            (self.closestpoint_x - self.ball_x) ** 2 + (self.closestpoint_y - self.ball_y) ** 2)

        if self.distance < self.radius and self.collision_sign_y == 1 and (self.collision_sign_x == 1 or self.collision_sign_x == 2):
            if self.collision_sign_x == 1:
                self.move_x = int(- self.speed * math.sin(math.pi / 4))
                self.move_y = int(self.speed * math.sin(math.pi / 4))
            if self.collision_sign_x == 2:
                self.move_x = int(self.speed * math.sin(math.pi / 4))
                self.move_y = int(self.speed * math.sin(math.pi / 4))

        # hit on the paddle

        if self.distance < self.radius and self.collision_sign_y == 1 and self.collision_sign_x == 3:
            theta = math.pi / 2 * \
                (1 - (self.ball_x - self.mouse_x) / self.paddle_width)
            self.move_x = int(self.speed * math.cos(theta))
            self.move_y = int(self.speed * math.sin(theta))

        # collision check when ball locate at left and right side of the rack
        if self.distance < self.radius and self.collision_sign_y == 3:
            if self.collision_sign_x == 1:

                self.move_x = int(- self.speed * math.cos(math.pi / 6))
                self.move_y = int(self.speed * math.sin(math.pi / 6))

            if self.collision_sign_x == 2:
                self.move_x = int(self.speed * math.cos(math.pi / 6))
                self.move_y = int(self.speed * math.sin(math.pi / 6))

    # Ball-brick:
    # The collision judgement function are the same as that of ball-paddle
    # need to find the nearest point of the rectangle to the ball.
    # The reflection condition is much easier: If hit horizontal part,
    # vy=-vy, if hit perpendicular part, vx=-vx, if hit the corner
    # change the sign of vx and vy at the same time.

    def ball_brick(self):
        # define the collision sign
        self.collision_sign_bx = 0
        self.collision_sign_by = 0

        if self.ball_x < self.brick_x:
            self.closestpoint_bx = self.brick_x
            self.collision_sign_bx = 1
        elif self.ball_x > self.brick_x + self.brick_width:
            self.closestpoint_bx = self.brick_x + self.brick_width
            self.collision_sign_bx = 2
        else:
            self.closestpoint_bx = self.ball_x
            self.collision_sign_bx = 3

        if self.ball_y < self.brick_y:
            self.closestpoint_by = self.brick_y
            self.collision_sign_by = 1
        elif self.ball_y > self.brick_y + self.brick_height:
            self.closestpoint_by = self.brick_y + self.brick_height
            self.collision_sign_by = 2
        else:
            self.closestpoint_by = self.ball_y
            self.collision_sign_by = 3
        # define the distance of the ball center and the brick edge
        self.distanceb = math.sqrt((
            self.closestpoint_bx - self.ball_x) ** 2 + (self.closestpoint_by - self.ball_y) ** 2)
        # collision check when ball is over the brick
        if self.distanceb < self.radius and self.collision_sign_by == 1 and (self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            if self.collision_sign_bx == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x > 0:
                self.move_y = - self.move_y
        if self.distanceb < self.radius and self.collision_sign_by == 1 and self.collision_sign_bx == 3:
            self.move_y = - self.move_y
        # collision check when ball is under the brick
        if self.distanceb < self.radius and self.collision_sign_by == 2 and (self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            if self.collision_sign_bx == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x > 0:
                self.move_y = - self.move_y
        if self.distanceb < self.radius and self.collision_sign_by == 2 and self.collision_sign_bx == 3:
            self.move_y = - self.move_y
        # collision check when the ball locate in left
        # and right side of the brick
        if self.distanceb < self.radius and self.collision_sign_by == 3:
            self.move_x = - self.move_x


class Score():

    # set the score object on top right of the screen, 10 points/brick

    def __init__(self, *args, **kw):
        # set up the initial score and the font
        self.score = 0
        self.score_font = pygame.font.SysFont('arial', 30)

    def countscore(self):
        # show the score
        my_score = self.score_font.render(
            str(self.score), False, (255, 255, 255))
        self.game_window.blit(my_score, (self.window_width - 45, 15))


class GameOver():
    # set the gameover sign and the indicator

    def __init__(self, *args, **kw):
        # set the font
        self.over_font = pygame.font.SysFont('arial', 80)
        self.gameover = self.over_font.render(
            "Game Over", False, (200, 200, 200))
        # set the sign
        self.over_sign = 0


class Win():
    # set the win sign and the indicator

    def __init__(self, *args, **kw):
        # set font for you win
        self.win_font = pygame.font.SysFont('arial', 80)
        self.win = self.win_font.render("You Win", False, (200, 200, 200))
        self.start_font = pygame.font.SysFont('arial', 30)
        self.start = self.start_font.render(
            'Please select the level of next game', False, (45, 186, 30))
        self.indicator_font = pygame.font.SysFont('arial', 70)
        self.indicator = self.start_font.render(
            'Casual            Normal            Advanced', False, (0, 95, 177))
        # set the win sign
        self.win_sign = 0


class Casual(GameWindow, Paddle1, Ball1, Brick, Collision, Score, Win, GameOver):
    # creat the game class for normal level, use Paddle1 and Ball1 class

    def __init__(self, *args, **kw):
        # use super function the enable the inheritance of the
        # variance between the classes.
        super(Casual, self).__init__(*args, **kw)
        super(GameWindow, self).__init__(*args, **kw)
        super(Paddle1, self).__init__(*args, **kw)
        super(Ball1, self).__init__(*args, **kw)
        super(Brick, self).__init__(*args, **kw)
        super(Collision, self).__init__(*args, **kw)
        super(Score, self).__init__(*args, **kw)
        super(Win, self).__init__(*args, **kw)
        # define the start game sign
        start_sign = 0
        while True:
            self.bgcolor()
            self.paddle_move()
            self.countscore()
            # if win or lose, break the loop
            if self.over_sign == 1 or self.win_sign == 1:
                break
            # read the status of game window, press to start the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    pressed_array = pygame.mouse.get_pressed()
                    if pressed_array[0]:
                        start_sign = 1
            # if the not started, initiate the ball, if started, move the ball
            if start_sign == 0:
                self.ballready()
            else:
                self.ballmove()
            self.brickarrange()
            # refresh the game window and control the refresh frequency
            pygame.display.update()
            time.sleep(0.010)


class Normal(GameWindow, Paddle2, Ball2, Brick, Collision, Score, Win, GameOver):
    # creat the game class for normal level, use Paddle2 and Ball2 class

    def __init__(self, *args, **kw):
        super(Normal, self).__init__(*args, **kw)
        super(GameWindow, self).__init__(*args, **kw)
        super(Paddle2, self).__init__(*args, **kw)
        super(Ball2, self).__init__(*args, **kw)
        super(Brick, self).__init__(*args, **kw)
        super(Collision, self).__init__(*args, **kw)
        super(Score, self).__init__(*args, **kw)
        super(Win, self).__init__(*args, **kw)
        start_sign = 0
        while True:
            self.bgcolor()
            self.paddle_move()
            self.countscore()
            if self.over_sign == 1 or self.win_sign == 1:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    pressed_array = pygame.mouse.get_pressed()
                    if pressed_array[0]:
                        start_sign = 1
            if start_sign == 0:
                self.ballready()
            else:
                self.ballmove()
            self.brickarrange()
            pygame.display.update()
            time.sleep(0.010)


class Advanced(GameWindow, Paddle3, Ball3, Brick, Collision, Score, Win, GameOver):
    # creat the game class for advanced level, use Paddle3 and Ball3 class

    def __init__(self, *args, **kw):
        super(Advanced, self).__init__(*args, **kw)
        super(GameWindow, self).__init__(*args, **kw)
        super(Paddle3, self).__init__(*args, **kw)
        super(Ball3, self).__init__(*args, **kw)
        super(Brick, self).__init__(*args, **kw)
        super(Collision, self).__init__(*args, **kw)
        super(Score, self).__init__(*args, **kw)
        super(Win, self).__init__(*args, **kw)
        start_sign = 0
        while True:
            self.bgcolor()
            self.paddle_move()
            self.countscore()
            if self.over_sign == 1 or self.win_sign == 1:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    pressed_array = pygame.mouse.get_pressed()
                    if pressed_array[0]:
                        start_sign = 1
            if start_sign == 0:
                self.ballready()
            else:
                self.ballmove()
            self.brickarrange()
            pygame.display.update()
            time.sleep(0.010)


def rungame():
    # The main game function, start the game, show the start interface
    # of the game. Load the background picture and the level options.
    # Create the button and load the objects for different level.
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([600, 500])
    pygame.display.set_caption("DX-Ball")
    screen.fill([0, 0, 0])
    myimage = pygame.image.load("bg.png")
    screen.blit(myimage, [0, 0])
    start_font = pygame.font.SysFont('arial', 30)
    start = start_font.render(
        'Please select the game level', False, (45, 186, 30))
    indicator = start_font.render(
        'Casual            Normal            Advanced', False, (0, 95, 177))
    screen.blit(start, (30, 350))
    screen.blit(indicator, (30, 400))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and 0 <= event.pos[0] <= 150 and 0 <= event.pos[1] <= 500:
                Casual()
            if event.type == pygame.MOUSEBUTTONDOWN and 151 <= event.pos[0] <= 300 and 0 <= event.pos[1] <= 500:
                Normal()
            if event.type == pygame.MOUSEBUTTONDOWN and 301 <= event.pos[0] <= 450 and 0 <= event.pos[1] <= 500:
                Advanced()


if __name__ == '__main__':
    rungame()
