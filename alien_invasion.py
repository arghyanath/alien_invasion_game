import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen,ai_settings)
    bullets = Group()
    aliens = Group()

    stats = GameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, aliens, ship)
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) # if gmae is inactive we still need to check other events
        
        if stats.game_active :
            ship.update()
            gf.update_bullets(ai_settings, screen, bullets, aliens, ship)
            gf.update_aliens(ai_settings, screen, stats, ship, bullets, aliens)
            gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()