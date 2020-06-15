import pygame
import GameModules

class GameScreen():
    """
    GameScreen class that is responsible for handling the game display.
    """
    __white_rgb_color = (255, 255, 255)
    __black_rgb_color = (0, 0, 0)
    __title = "Snakker"
    __tick_rate = 60
    __clock = pygame.time.Clock()
    __is_shutdown = False
    __player_img = "../resources/player.png"
    
    def __init__(self, screen_width = 800, screen_height = 800):
        """
        Creates GameScreen object and initializes pygame.

        Parameters
        ----------
        screen_width : int
            Sets the displayed screen width

        screen_height : int
            Sets the displayed screen height
        """
        pygame.init()

        self.__width = screen_width
        self.__height = screen_height


    def change_screen_size(self, screen_width, screen_height):
        """
        Allows to change screen size.

        Parameters
        ----------
        screen_width : int
            Sets the displayed screen width

        screen_height : int
            Sets the displayed screen height
        """
        self.__width = screen_width
        self.__height = screen_height


    def handle_display(self):
        """
        Handles the display loop and shutdown event.

        Returns
        -------
        Bool
            True if no errors, false otherwise.
        """
        player = GameModules.PlayerObject(self.__player_img, 375, 700, 50, 50)
        direction = 0

        if not self.__init_display():
            print("There were problems initializing the display.")
            return False

        while not self.__is_shutdown:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    self.__is_shutdown = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #move up
                        direction = -1
                    elif event.key == pygame.K_DOWN:
                        #move down
                        direction = 1

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        #move down
                        direction = 0

            player.move(direction)
            self.game_screen.fill(self.__white_rgb_color)
            player.draw(self.game_screen)

            pygame.display.update()
            self.__clock.tick(self.__tick_rate)            
        
        return True


    def set_fps(self, fps):
        """
        Sets custom FPS value. Default is 60
        """
        if fps > 60:
            print("FPS can't be higher than 60")
            return

        self.__tick_rate = fps


    def __init_display(self):
        """
        Initializes game screen display.

        Returns
        -------
        Bool
            True if no errors, false otherwise.
        """
        if self.__width < 100 or self.__height < 100:
            print("Screen size is too small!")
            return False
        else:
            self.game_screen = pygame.display.set_mode((self.__width, self.__height))
            self.game_screen.fill(self.__white_rgb_color)
            
            pygame.display.set_caption(self.__title)
            return True

