import sys
import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
import game_function as gf

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship.
    ship = Ship(screen)
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in.
    bullets = Group()

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_setting, screen, ship, bullets)

    #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
