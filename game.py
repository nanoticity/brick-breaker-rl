import pygame as pg

class Brick:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.dimensions = (76, 20)
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.color.Color("black"), self.rect)

    def is_collide(self, ball) -> bool:
        ball_rect = pg.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
        is_collide = self.rect.colliderect(ball_rect)
        if is_collide:
            ball.y_add *= -1
        return is_collide

class BrickManager:
    def __init__(self):
        self.bricks = []
    
    def create_bricks(self):
        for y in range(5):
            for x in range(10):
                self.bricks.append(Brick(x*80+2, y*24+2))
    
    def draw_bricks(self, surface, ball):
        for brick in self.bricks:
            if brick.is_collide(ball):
                self.bricks.remove(brick)
                continue
            brick.draw(surface)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_add = 8
        self.y_add = 5
        self.radius = 10
        self.hit = False
        self.initial_values = (x, y, self.x_add, self.y_add)

    def move(self, paddle):
        self.x += self.x_add
        self.y += self.y_add
        
        self.collisions_handler(paddle)
        
    def collisions_handler(self, paddle):
        if self.x <= 0 + self.radius or self.x >= 800 - self.radius:
            self.x_add *= -1
        
        if self.y <= 0 + self.radius:
            self.y_add *= -1
        
        if not self.hit:
            if self.y >= 760 - self.radius and self.y <= 780 - self.radius:
                if self.x >= paddle.x and self.x <= paddle.end_x:
                    distance_from_center = self.x - paddle.middle_x
                    # Bound distance from center to the range (-89, 89)
                    distance_from_center = max(-89, min(89, distance_from_center))
                    self.x_add = distance_from_center / 5
                    self.y_add *= -1
                    self.hit = True
        
        if self.y <= 400:
            self.hit = False
            
        if self.y >= 800 + self.radius:
            self.reset()
            
    def reset(self):
        pg.time.wait(100)
        self.x = self.initial_values[0]
        self.y = self.initial_values[1]
        self.x_add = self.initial_values[2]
        self.y_add = self.initial_values[3]

    def draw(self, surface):
        pg.draw.circle(surface, pg.color.Color("black"), (self.x, self.y), self.radius)

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.middle_x = self.x + self.width / 2
        self.end_x = self.x + self.width

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= 10
        if keys[pg.K_RIGHT]:
            self.x += 10

        max_x = 800 - self.width
        if self.x < 0:
            self.x = 0
        elif self.x > max_x:
            self.x = max_x

        self.position_update()
            
    def position_update(self):
        self.middle_x = self.x + self.width / 2
        self.end_x = self.x + self.width
        print(self.end_x)

    def draw(self, surface):
        pg.draw.line(surface, pg.color.Color("black"), (self.x, self.y), (self.end_x, self.y), 20)

