import pygame
import random

pygame.init()

width , height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("King of gamblers")

game_started = False
difficulty_selected = False
difficulty = ""

