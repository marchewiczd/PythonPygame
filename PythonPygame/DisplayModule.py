import pygame

__title = "Snakker"
__tick_rate = 60
__height = 800
__width = 800
__game_screen = pygame.display.set_mode((__width, __height))


def set_screen_size(screen_width, screen_height):
    """
    Allows to set screen size.

    Parameters
    ----------
    screen_width : int
        Sets the displayed screen width

    screen_height : int
        Sets the displayed screen height
    """
    global __width
    global __height

    __width = screen_width
    __height = screen_height


def handle_display():
    """
    Handles the display loop and shutdown event.
    """
    global __tick_rate

    is_shutdown = False
    clock = pygame.time.Clock()

    if not __init_display():
        print("There were problems initializing the display.")
        return False

    while not is_shutdown:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                is_shutdown = True

        pygame.display.update()
        clock.tick(__tick_rate)

    pygame.quit()

    return True


def set_fps(fps):
    """
    Sets custom FPS value. Default is 60
    """
    global __tick_rate

    if fps > 60:
        print("FPS can't be higher than 60")
        return

    __tick_rate = fps


def __init_display():
    """
    Initializes game screen display.

    Returns
    -------
    Bool
        True if no errors, false otherwise.
    """

    global __width
    global __height
    global __game_screen
    white_rgb_color = (255, 255, 255)

    if __width < 100 or __height < 100:
        print("Screen size is too small!")
        return False
    else:
        __game_screen.fill(white_rgb_color)
        pygame.display.set_caption(__title)
        return True

