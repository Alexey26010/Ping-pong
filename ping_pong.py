from random import randint
from pygame import *
window = display.set_mode((900, 600))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('4294820.jpg'), (900, 600))
class GameSprite(sprite.Sprite):
    def __init__(self, palyer_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(palyer_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed
player_1 = Player('square.png', 40, 270, 10, 15, 95)
player_2 = Player('square.png', 825, 270, 10, 15, 95)
ball = GameSprite('free-icon-ball-802340.png', 425, 300, 15, 50, 50)
font.init()
font2 = font.SysFont('Arial Black', 80)
lose1 = font2.render('Player 1 LOSE', True, (180, 0, 0))
lose2 = font2.render('Player 2 LOSE', True, (180, 0, 0))
game = True
finish = False
l = [-3, 3]
speed_x = l[randint(0, 1)]
speed_y = l[randint(0, 1)]
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        player_1.reset()
        player_1.update_l()
        player_2.reset()
        player_2.update_r()
        ball.reset()
        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if ball.rect.y > 600 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 900:
            finish = True
            window.blit(lose2, (200, 200))
        display.update()
    else:
        finish = False
        ball.rect.x = 425
        ball.rect.y = 300
        player_1.rect.x = 40
        player_1.rect.y = 270
        player_2.rect.x = 825
        player_2.rect.y = 270
        speed_x = l[randint(0, 1)]
        speed_y = l[randint(0, 1)]
        time.delay(3000)
    time.delay(50)