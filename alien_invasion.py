import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_function as gf
from button import Button

def run_game():
    #initialize game and greate a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings,screen,"Play")

    stats = GameStats(ai_settings)

    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    #start game loops:
    while True:
        #monitor keyboard and mouse event
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)
        


run_game()
