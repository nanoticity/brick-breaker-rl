from typing import Optional
import numpy as np
import gymnasium as gym
import pygame as pg
from game import *

class BrickBreakerEnv:
    def __init__(self):
        self.screen = pg.display.set_mode([800, 800])
        self.brick_manager = BrickManager()
        self.brick_manager.create_bricks()
        self.paddle = Paddle(350, 760)
        self.ball = Ball(300, 500)
        self.clock = pg.time.Clock()
        self.run = True

    def reset(self):
        self.brick_manager = BrickManager()
        self.brick_manager.create_bricks()
        self.paddle = Paddle(350, 760)
        self.ball = Ball(300, 500)

    def step(self, action):
        if action == 0:
            self.paddle.move_left()
        elif action == 1:
            self.paddle.move_right()

        self.ball.move(self.paddle)
        self.render()

    def render(self):
        self.screen.fill(pg.color.Color("white"))
        self.brick_manager.draw_bricks(self.screen, self.ball)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        pg.display.update()
        self.clock.tick(60)

    def close(self):
        pg.quit()