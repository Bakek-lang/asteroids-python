# import pygame
# from constants import *


# def draw_text(text, position, screen):
#     font = pygame.font.Font(None, 36)
#     text_surface = font.render(text, True, "white")
#     screen.blit(text_surface, position)

# def handle_menu(screen):
#     global game_state
#     screen.fill("black")

#     draw_text("Click to Play", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), screen)


#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             game_state = PLAYING
