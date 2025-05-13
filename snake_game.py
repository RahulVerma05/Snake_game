#improt req libraries
import pygame
import time
import random

snake_speed = 20

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
snake_postion = [50,50]

snake_body_postion = [ [50,50],
                      [60,50],
                      [70,50],
                      [80,50] ]

#ball postion
ball_postion = [random.randrange(1,(window_wide//10)*10),
                random.randrange(1,(window_height//10)*10)]

ball_change = True

mouth_direction = 'Left'
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
    g_font = pygame.font('times new roman',50)
    #game over surface to display 
    game_over_surface = g_font.render('Your Score : ' + str(score),True, red)
    #rectangular box to display
    game_over_box = game_over_surface.get_react()
    #place to game over box display
    game_over_box.midtop = (window_wide/2, window_height/4)
    #text display
    game_window.blit(game_over_surface,game_over_box)
    pygame.display.flip()
    #time to quit
    time.sleep(5)
    #quit the program
    pygame.quit()
    quit()

