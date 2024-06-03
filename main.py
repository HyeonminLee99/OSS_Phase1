import pygame
import random

pygame.init()

width , height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("King of gamblers")


font = pygame.font.Font(None, 74)

black = (0,0,0)

game_started = False
difficulty_selected = False
difficulty = ""
asset = 0

running = True

def draw_text(text , font, color ,surface , x, y ) :
    text_obj = font.render(text, True , color)
    textrect = text_obj.get_rect()
    textrect.center = (x,y)
    surface.blit(text_obj , textrect)



"""
while running :
"""


if not game_started :
    draw_text("Let's Gamble" , font , black , screen , width//2 , height//2)