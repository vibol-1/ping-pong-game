from pygame import *

from spriteClass import GameSprite, Player

''' colors '''
background = (200, 255, 255)

window = display.set_mode((600, 500)) # widht, height
window.fill(background)

clock = time.Clock()

platform_left = Player('image/racket.png', 10, 220, 4, 50, 150)
platform_right = Player('image/racket.png', 500, 220, 4, 50, 150)
ball = GameSprite(player_image='image/tenis_ball.png', player_x=200, player_y=200, player_speed=4, wight=50, height=50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

''' variables '''
game = True
speed_x = 3
speed_y = 3
finish = True

'''' game loop '''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == True:
        window.fill(background) # keep refreshing the window

        ball.reset(window_object=window)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(platform_left, ball) or sprite.collide_rect(platform_right, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1

        # lose condition
        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = False
        if ball.rect.x > 550:
            window.blit(lose2, (200, 200))
            finish = False

        platform_left.reset(window_object=window)
        platform_left.update_left()
        platform_right.reset(window_object=window)
        platform_right.update_right()
    

    display.update()
    clock.tick(60) # 60 frame per second