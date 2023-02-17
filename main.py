import pygame, sys, random


def ball_animation():
    global ball_speed_x,ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))



#general setup
pygame.init() #initiates all pygame modules
clock = pygame.time.Clock() #clock method stores in clock

#setting up main window
screen_width = 1280
screen_height = 960

#code to create the display surface object, can only be one
screen = pygame.display.set_mode((screen_width,screen_height))

#game rectangles
ball = pygame.Rect(screen_width/2 - 17.5,screen_height/2 - 17.5,35,35)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

ball_colour = pygame.Color('blue')
bg_colour = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #closes the game is user decides to quit
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()


    #visuals
    screen.fill((0,0,0))
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.draw.ellipse(screen, ball_colour, ball)

    #updating the window
    pygame.display.flip()
    clock.tick(60)