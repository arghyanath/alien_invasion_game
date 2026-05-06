import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


# bullets fuctions
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)

def check_bullet_collision(ai_settings, screen, bullets, aliens, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # 1st True -> to delete and 2nd True -> to delete alien 
    
    # if all aliens eliminated, delete all bullets and respawn another fleet
    if len(aliens) == 0: 
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)

def update_bullets(ai_settings, screen, bullets, aliens, ship):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    
    # checking for any collisions of bullet with alien
    check_bullet_collision(ai_settings, screen, bullets, aliens, ship)

    
                                                       

# alien fuctions
def get_number_aliens_x(ai_settings, screen, alien_width):
    available_space_x = ai_settings.screen_width - 2 *  alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))
    return number_of_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, alien_number, row_number, aliens):
    alien = Alien(screen, ai_settings)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.y = alien.rect.height + 2* alien.rect.height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    number_rows = get_number_rows(ai_settings, alien_height, ship.rect.height)
    number_of_aliens_x = get_number_aliens_x(ai_settings, screen, alien_width)

    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(ai_settings, screen, alien_number, row_number, aliens)

def change_fleet_direction(ai_settings, aliens):
    # drop the entire fleet and change fleet direction 
    for alien in  aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    # check if any alien hit the edge then change fleet direction
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def ship_hit(ai_settings, screen, stats, ship, bullets, aliens):
    
    if stats.ships_left > 0 :
        stats.ships_left -= 1 # decrement numbers of ships left

        # delete all the aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new alien fleet and center the ship 
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        # if no ship left Game Over
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_alien_hit_bottom(ai_settings, screen, stats, ship, bullets, aliens):
    # do same as ship_hit
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, ship, bullets, aliens)

def update_aliens(ai_settings, screen, stats, ship, bullets, aliens):
    # check if the fleet hit the edge and update postions of all aliens
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien - ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, bullets, aliens)

    # check if any alien reaches the bottom then
    check_alien_hit_bottom(ai_settings, screen, stats, ship, bullets, aliens)

    
# keyboard and mouse event functions / ship movements

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
            ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def click_play_button(ai_settings, screen, stats,  aliens, ship, bullets, 
                        play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active : # activate play button only whem game is not activate
        stats.game_active = True
        pygame.mouse.set_visible(False)
        # reset game
        stats.reset_stats()

        aliens.empty() 
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
    

def check_events(ai_settings, screen, stats, play_button, aliens, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            click_play_button(ai_settings, screen, stats,  aliens, ship, bullets, 
                        play_button, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button):
    screen.fill(ai_settings.bg_color) 
    for bullet in bullets:
        bullet.draw_bullet() 
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()