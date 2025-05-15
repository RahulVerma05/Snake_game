#improt req libraries
import pygame
import time
import random

snake_speed = 10

# game window size
window_wide = 720
window_height = 480

# colour
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#Game initialising
pygame.init()

#game window
pygame.display.set_caption('snake trail')
game_window = pygame.display.set_mode((window_wide, window_height))

fps = pygame.time.Clock()

#Snake position at intial
snake_position = [100,50]

snake_body =        [ [100,50],
                      [90,50],
                      [80,50], ]

#ball position
ball_position = [200,200]

ball_change = True

mouth_direction = 'Right'
change_to = mouth_direction

#Scoreboard
score = 0
#function for scoreboard
def show_score(choice, color, font, size):
    #function for score font
    score_font = pygame.font.SysFont(font,size)
    #surface object to display
    score_surface = score_font.render('Score : '+str(score), True, color)
    #rectangular box for score
    score_box = score_surface.get_rect()
    #text display
    game_window.blit(score_surface,score_box)

#Game over function

def game_over():
    #Game over font
    g_font = pygame.font.SysFont('times new roman', 50)
    #game over surface to display 
    game_over_surface = g_font.render('Your Score : ' + str(score),True, red)
    #rectangular box to display
    game_over_box = game_over_surface.get_rect()
    #place to game over box display
    game_over_box.midtop = (window_wide/2, window_height/4)
    #text display
    game_window.blit(game_over_surface,game_over_box)
    pygame.display.flip()
    #time to quit
    time.sleep(3)
    #quit the program
    pygame.quit()
    quit()

#main game function

while True:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    #if two keys pressed simultaneously
    #for snake to move in one direction
    if change_to == 'UP' and mouth_direction != 'DOWN':
        mouth_direction = 'UP'
    if change_to == 'DOWN' and mouth_direction != 'UP':
        mouth_direction = 'DOWN'
    if change_to == 'LEFT' and mouth_direction != 'RIGHT':
        mouth_direction = 'LEFT'
    if change_to == 'RIGHT' and mouth_direction != 'LEFT':
        mouth_direction = 'RIGHT'

    #snake position
    if mouth_direction == 'UP':
        snake_position[1] -= 10
    if mouth_direction == 'DOWN':
        snake_position[1] += 10
    if mouth_direction == 'LEFT':
        snake_position[0] -= 10
    if mouth_direction == 'RIGHT':
        snake_position[0] += 10
    
    #snake body growing mechanism
    #if food eaten
    snake_body.insert(0,list(snake_position))
    if snake_position[0] == ball_position[0] and snake_position[1] == ball_position[1]:
        score += 10
        ball_change = False
    else:
        snake_body.pop()
    
    if not ball_change:
        ball_position = [random.randrange(1,(window_wide//10))*10,
                        random.randrange(1,(window_height//10))*10]
    
    ball_change = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(ball_position[0], ball_position[1], 10, 10))
    #Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_wide-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_height-10:
        game_over()
    #touching itself
    if len(snake_body) > 3:
        #if snake head touches the body
        #game over
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
    #show score
    show_score(1, white, 'times new roman', 20)
    #refresh game screen
    pygame.display.update()
    #frame per second
    fps.tick(snake_speed)
#end of game
#quit the game  