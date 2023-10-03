import pygame
import sys
import settings_menu
from main import Game


# initializing the constructor
pygame.init()
# screen resolution
res = (1280, 720)
# opens up a window
screen = pygame.display.set_mode(res)
# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)
# stores the width of the
# screen into a variable
width = screen.get_width()
# stores the height of the
# screen into a variable
height = screen.get_height()
# defining a font
smallfont = pygame.font.SysFont("Corbel", 35)
# rendering a text written in
# this font
text_start = smallfont.render("start", True, color)
text_settings = smallfont.render("settings", True, color)
text_quit = smallfont.render("quit", True, color)


def start_game():
    game = Game()
    game.run()


def quit_game():
    pygame.quit()
    sys.exit()


def open_settings():
    settings_menu.main()


while True:
    # fills the screen with a color
    screen.fill((60, 25, 60))
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # if mouse is hovered on a button it changes to lighter shade
    if (
        width / 2 <= mouse[0] <= width / 2 + 140
        and height / 2 <= mouse[1] <= height / 2 + 40
    ):
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
    # superimposing the text onto our button
    screen.blit(text_start, (width / 2 + 50, height / 2))
    # creating quit button
    if (
        width / 2 <= mouse[0] <= width / 2 + 140
        and height / 2 + 50 <= mouse[1] <= height / 2 + 90
    ):
        pygame.draw.rect(screen, color_light, [width / 2, height / 2 + 50, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2 + 50, 140, 40])
    # superimposing the text onto our button
    screen.blit(text_quit, (width / 2 + 50, height / 2 + 50))
    # creating settings button
    if (
        width / 2 <= mouse[0] <= width / 2 + 140
        and height / 2 + 100 <= mouse[1] <= height / 2 + 140
    ):
        pygame.draw.rect(screen, color_light, [width / 2, height / 2 + 100, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2 + 100, 140, 40])
    # superimposing the text onto our button
    screen.blit(text_settings, (width / 2 + 50, height / 2 + 100))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit_game()
        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the start button the game is started
            if (
                width / 2 <= mouse[0] <= width / 2 + 140
                and height / 2 <= mouse[1] <= height / 2 + 40
            ):
                start_game()
            # if the mouse is clicked on the quit button the game is terminated
            if (
                width / 2 <= mouse[0] <= width / 2 + 140
                and height / 2 + 50 <= mouse[1] <= height / 2 + 90
            ):
                quit_game()
            # if the mouse is clicked on the settings button the settings are opened
            if (
                width / 2 <= mouse[0] <= width / 2 + 140
                and height / 2 + 100 <= mouse[1] <= height / 2 + 140
            ):
                open_settings()
    # updates the frames of the game
    pygame.display.update()
