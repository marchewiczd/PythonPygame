import pygame

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

    def change_speed(self, speed):
        self.__speed = speed

    def check_bounds(self, x_pos, y_pos):
        return


class PlayerObject(GameObject):
    __speed = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction == 0:
            return

        if direction != 1 and direction != -1:
            print("Direction should be either -1 or 1")
            return

        if direction == 1 and self.y_pos >= max_height - 50:
            return
        elif direction == -1 and self.y_pos <= 10:
            return 
            
        self.y_pos += direction * self.__speed


class NpcObject(GameObject):
    __speed = 10
    __direction = 1

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.__direction = 1
        elif self.x_pos >= max_width - 70:
            self.__direction = -1
        
        self.x_pos += self.__direction * self.__speed