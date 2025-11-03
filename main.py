import pygame as pg
from game import *

pg.init()

def main():
    screen = pg.display.set_mode([800, 800])
    
    brick_manager = BrickManager()
    brick_manager.create_bricks()
    
    paddle = Paddle(350, 760)
    
    ball = Ball(300, 500)
    
    clock = pg.time.Clock()

    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False
                
        screen.fill(pg.color.Color("white"))
        brick_manager.draw_bricks(screen)
        
        paddle.draw(screen)
        paddle.move()
        
        ball.draw(screen)
        ball.move(paddle)

        pg.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
