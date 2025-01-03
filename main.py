import sys
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from bullets import Shot
from enum import Enum, auto


class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()

# drawing functions

def draw_menu(screen):
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 74)
    text = font.render('Click to Start', True, (255, 255, 255))
    global start_button_rect
    start_button_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, start_button_rect)

def draw_game(screen, drawable):
    screen.fill((0, 0, 0))
    for obj in drawable:
        obj.draw(screen)

def draw_game_over(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over! Click to return to START', True, (255, 255, 255))
    global restart_button_rect
    restart_button_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, restart_button_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids(Bubble) Game") 

    current_state = GameState.MENU

    print("Starting asteroids!")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if current_state == GameState.MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        current_state = GameState.PLAYING
            
            elif current_state == GameState.GAME_OVER:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        return main()

        if current_state == GameState.PLAYING:
            for obj in updatable:
                obj.update(dt)

            for asteroid in asteroids:
                if asteroid.collision(player):
                    current_state = GameState.GAME_OVER

                for shot in shots:
                    if asteroid.collision(shot):
                        asteroid.split()
                        shot.kill()


        screen.fill("black")

        if current_state == GameState.MENU:
            draw_menu(screen)
        if current_state == GameState.PLAYING:
            draw_game(screen, drawable)
        elif current_state == GameState.GAME_OVER:
            draw_game_over(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
