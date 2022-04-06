from pygame import*
from random import randint


class Game_sprite(sprite.Sprite):
    def __init__(self, image, x, y, w, h):
        super().__init__()
        self.image=  transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self.rect)

class Platform(Game_sprite):
    def __init__(self):
        super().__init__(image.load('platform.jpg'), 300, 390, 150, 50)
        
    def update(self):
        keypressed = key.get_pressed()
        if keypressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x += 3
        if keypressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 3
        screen.blit(self.image, self.rect)
        super().update()
    

class Block(Game_sprite):
    def __init__(self, x ,y ):
        super().__init__(image.load('block.png'), x, y, 100, 50)
    def update(self):
        super().update()
        

class Ball(Game_sprite):
    def __init__(self):
        super().__init__(image.load('ball.png'), 350, 200, 20, 20)
        self.x = 3
        self.y = -3
    def update(self, platform, block_group):
        self.rect.x += self.x
        self.rect.y += self.y

        if self.rect.x <= 0 or self.rect.x >= 780:
            self.x *= -1
        if self.rect.y <= 0:
            self.y = 3
        if self.rect.colliderect(platform.rect):
            self.y = -3
        if sprite.spritecollideany(self, block_group):
            self.y *= -1
        
        
        super().update()
        

display.set_caption('MYGAME')
screen = display.set_mode((800,500))
background = image.load('way.png')
block_group = sprite.Group()
block_img = image.load('block.png')
background = transform.scale(background, (800,500))
button_play = transform.scale(image.load('play.png'), (200, 80))
button_quit = transform.scale(image.load('quit.png'), (200, 80))

ball = Ball()
platform = Platform()
x = 0
for i in range(8):
    block = Block(x, 10)
    block_group.add(block)
    x += 100


clock = time.Clock()
game = True
menu = True
finish = True

while game:
    clock.tick(60)
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x, y = mouse.get_pos()
                if menu:
                    if x > 300 and x < 500 and y > 200 and y < 280:
                        menu = False
                        finish = False
                    if x > 300 and x < 500 and y > 300 and y < 380:
                        game = False




    screen.blit(background, (0,0))
    if menu:
        screen.blit(button_play, (300, 200))
        screen.blit(button_quit, (300, 300))
    elif not(finish):
        platform.update()
        for block in block_group:
            block.update()
        ball.update(platform, block_group)
    display.update()