import pygame.font
class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.height, self.width = 50, 200
        self.button_color = (200, 200, 200)
        self.text_color = (28,37,60)
        self.font =  pygame.font.SysFont(None, 48)

        # creating button's rect object an center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button's msg need to be prepped only once
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        # turn the text stored in msg into an image
        self.msg_image = self.font.render(msg, True, # antialiasing -> True
                            self.text_color, self.button_color) # text color ,text background color
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) # draw a rectangle
        self.screen.blit(self.msg_image, self.msg_image_rect) # draw image inside the rectangle

