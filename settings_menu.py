# Python program to create a basic settings menu using the pygame_menu module

import pygame
import pygame_menu as pm
import sys
from main import Game
import start_menu

pygame.init()

# Screen
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Standard RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main function of the program
def main():
    # List that is displayed while selecting the window resolution level
    resolution = [
        ("1920x1080", "1920x1080"),
        ("1920x1200", "1920x1200"),
        ("1280x720", "1280x720"),
        ("2560x1440", "2560x1440"),
        ("3840x2160", "3840x2160"),
    ]

    # List that is displayed while selecting the difficulty
    difficulty = [("Easy", "Easy"), ("Medium", "Medium"), ("Expert", "Expert")]

    # List that is displayed while selecting the player's perspective
    perspectives = [("FPP", "fpp"), ("TPP", "tpp")]

    in_game = False

    # This function displays the currently selected options
    def printSettings():
        print("\n\n")
        # getting the data using "get_input_data" method of the Menu class
        settingsData = settings.get_input_data()

        for key in settingsData.keys():
            print(f"{key}\t:\t{settingsData[key]}")

    # Creating the settings menu
    settings = pm.Menu(
        title="Settings", width=WIDTH, height=HEIGHT, theme=pm.themes.THEME_GREEN
    )

    # Adjusting the default values
    settings._theme.widget_font_size = 25
    settings._theme.widget_font_color = BLACK
    settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

    # Text input that takes in the username
    settings.add.text_input(title="User Name : ", textinput_id="username")

    # 2 different Drop-downs to select the graphics level and the resolution level
    settings.add.dropselect_multiple(
        title="Window Resolution",
        items=resolution,
        dropselect_multiple_id="Resolution",
        open_middle=True,
        max_selected=1,
        selection_box_height=6,
    )

    # Toggle switches to turn on/off the music and sound
    settings.add.toggle_switch(title="Muisc", default=True, toggleswitch_id="music")
    settings.add.toggle_switch(title="Sounds", default=False, toggleswitch_id="sound")

    # Selector to choose between the types of difficulties available
    settings.add.selector(
        title="Difficulty\t", items=difficulty, selector_id="difficulty", default=0
    )

    # Range slider that lets to choose a value using a slider
    settings.add.range_slider(
        title="FOV",
        default=60,
        range_values=(50, 100),
        increment=1,
        value_format=lambda x: str(int(x)),
        rangeslider_id="fov",
    )

    # Fancy selector (style added to the default selector) to choose between
    # first person and third person perspectives
    settings.add.selector(
        title="Perspective",
        items=perspectives,
        default=0,
        style="fancy",
        selector_id="perspective",
    )

    # clock that displays the current date and time
    settings.add.clock(
        clock_format="%d-%m-%y %H:%M:%S", title_format="Local Time : {0}"
    )

    # Button to print the current settings
    settings.add.button(
        title="Print Settings",
        action=printSettings,
        font_color=WHITE,
        background_color=GREEN,
    )

    # Button to reset settings to defaults
    settings.add.button(
        title="Restore Defaults",
        action=settings.reset_value,
        font_color=WHITE,
        background_color=RED,
    )

    def returnToMainMenu():
        nonlocal in_game
        in_game = False
        # Return to the start menu
        print("Returning to the start menu...")
        # Add your start menu code here
        return start_menu.main()

    settings.add.button(
        title="Return To Main Menu",
        action=returnToMainMenu,
        align=pm.locals.ALIGN_CENTER,
    )
    # Let us loop the settings menu on the screen

    def returnToGame():
        nonlocal in_game
        in_game = True
        print("Returning to the game...")
        return Game().run()
        # Add your game code here

    settings.add.button(
        title="Return To Game", action=returnToGame, align=pm.locals.ALIGN_CENTER
    )

    settings.mainloop(screen)


if __name__ == "__main__":
    main()
