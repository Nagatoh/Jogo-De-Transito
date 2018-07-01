import pygame
from pygame.locals import *
from game import *
from functions import *
from sys import exit
import os


class Menu:
    def __init__(self):
        self.background = load_image('menu_background.bmp')

        self.game_buttons = load_image('novo_jogo.png', 2, [((x,0),(186,76))\
                                             for x in xrange(0, 558, 186)])

        self.game_level = None
        self.car_type = 1

        self.game_button = self.game_buttons[0]
        self.game_size = self.game_button.get_size()
        self.game_pos = (35, 405)

        self.credits_buttons = load_image('creditos.png', 2, [((x,0),(140,70))\
                                             for x in xrange(0, 420, 140)])

        self.credits_buttton = self.credits_buttons[0]
        self.credits_size = self.credits_buttton.get_size()
        self.credits_pos = (570, 566)

        self.help_buttons = load_image('ajuda.png', 2, [((x,0),(26,118))\
                                             for x in xrange(0, 78, 26)])
        self.help_button = self.help_buttons[0]
        self.help_size = self.help_button.get_size()
        self.help_pos = (678, 40)

        self.exit_buttons = load_image('sair.png', 2, [((x,0),(111,74))\
                                             for x in xrange(0, 333, 111)])
        self.exit_button = self.exit_buttons[0]
        self.exit_size = self.exit_button.get_size()
        self.exit_pos = (228, 125)


        self.back_buttons = load_image('voltar.png', 2, [((0,y),(134,36))\
                                             for y in xrange(0, 108, 36)])
        self.back_button = self.exit_buttons[0]
        self.back_size = self.exit_button.get_size()
        self.back_pos = (50, 720)

        self.pressed = False

        self.fullscreen = True

    def set_fullscreen(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LALT] and pressed_keys[K_RETURN]:
            self.fullscreen = not self.fullscreen

            if self.fullscreen: screen = pygame.display.set_mode((pygame.display.Info().current_w,
                                  pygame.display.Info().current_h),
                                  pygame.FULLSCREEN)
            else: screen = pygame.display.set_mode((1024,768), 0, 32)

    def main_menu(self):
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load('sounds' + os.sep + 'game_music.mp3')
        #pygame.mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            self.set_fullscreen()

            self.background = load_image('menu_background.bmp')
            screen.blit(self.background, (0, 0))
                    

            # Verifica se os botoes esta sendo pressionados e muda as imagens
            # -Novo jogo
            if self.game_pos[0] <= mouse_pos[0] <= self.game_pos[0] + self.game_size[0]\
            and self.game_pos[1] <= mouse_pos[1] <= self.game_pos[1] + self.game_size[1]:

                self.game_button = self.game_buttons[1]

                if mouse_press[0]:
                    self.game_button = self.game_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.game_button = self.game_buttons[1]
                    #pygame.mixer.music.stop()
                    self.select_car_menu()

            else: self.game_button = self.game_buttons[0]

            # -Creditos
            if self.credits_pos[0] <= mouse_pos[0] <= self.credits_pos[0] + self.credits_size[0]\
            and self.credits_pos[1] <= mouse_pos[1] <= self.credits_pos[1] + self.credits_size[1]:

                self.credits_button = self.credits_buttons[1]

                if mouse_press[0]:
                    self.credits_button = self.credits_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.credits_button = self.credits_buttons[1]
                    self.credits_menu()

            else: self.credits_button = self.credits_buttons[0]

            # -Ajuda
            if self.help_pos[0] <= mouse_pos[0] <= self.help_pos[0] + self.help_size[0]\
            and self.help_pos[1] <= mouse_pos[1] <= self.help_pos[1] + self.help_size[1]:

                self.help_button = self.help_buttons[1]

                if mouse_press[0]:
                    self.help_button = self.help_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.help_button = self.help_buttons[1]
                    self.help_menu()

            else: self.help_button = self.help_buttons[0]

            # -Sair
            if self.exit_pos[0] <= mouse_pos[0] <= self.exit_pos[0] + self.exit_size[0]\
            and self.exit_pos[1] <= mouse_pos[1] <= self.exit_pos[1] + self.exit_size[1]:

                self.exit_button = self.exit_buttons[1]

                if mouse_press[0]:
                    self.exit_button = self.exit_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.exit_button = self.exit_buttons[1]
                    exit()

            else: self.exit_button = self.exit_buttons[0]

            if not mouse_press[0]:
                self.pressed = False

            #for button in menu.buttons:
            screen.blit(self.game_button, self.game_pos)
            screen.blit(self.credits_button, self.credits_pos)
            screen.blit(self.help_button, self.help_pos)
            screen.blit(self.exit_button, self.exit_pos)

            pygame.display.flip()

    def credits_menu(self):        
        self.background = load_image('menu_background_2.bmp')
        self.text = load_image('menu_creditos.bmp', 2)

        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.set_fullscreen()

            screen.blit(self.background, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            if self.back_pos[0] <= mouse_pos[0] <= self.back_pos[0] + self.back_size[0]\
            and self.back_pos[1] <= mouse_pos[1] <= self.back_pos[1] + self.back_size[1]:
                self.back_button = self.back_buttons[1]

                if mouse_press[0]:
                    self.back_button = self.back_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.back_button = self.back_buttons[1]
                    return

            else: self.back_button = self.back_buttons[0]

            if not mouse_press[0]:
                self.pressed = False

            screen.blit(self.text, (0, 0))
            screen.blit(self.back_button, self.back_pos)

            pygame.display.flip()

    def help_menu(self):
        self.background = load_image('menu_background_2.bmp')
        self.text = load_image('menu_ajuda.bmp', 2)

        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.set_fullscreen()

            screen.blit(self.background, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            if self.back_pos[0] <= mouse_pos[0] <= self.back_pos[0] + self.back_size[0]\
            and self.back_pos[1] <= mouse_pos[1] <= self.back_pos[1] + self.back_size[1]:
                self.back_button = self.back_buttons[1]

                if mouse_press[0]:
                    self.back_button = self.back_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.back_button = self.back_buttons[1]
                    return

            else: self.back_button = self.back_buttons[0]

            if not mouse_press[0]:
                self.pressed = False

            screen.blit(self.text, (0, 0))
            screen.blit(self.back_button, self.back_pos)

            pygame.display.flip()

    def select_car_menu(self):
        #pygame.mixer.music.stop()
       # pygame.mixer.music.load('sounds' + os.sep + 'select_menu.mp3')
       # pygame.mixer.music.play()
        
        self.background = load_image('menu_background_2.bmp')
        self.text = load_image('sel_carro.bmp', 2)

        self.car_selected = None

        self.list_button1 = load_image('carro1_atributos.png', 2, [((0,y),(445,180))\
                                                        for y in xrange(0, 540, 180)])
        self.button1_image = self.list_button1[0]
        self.button1_pos = (50, 100)

        self.list_button2 = load_image('carro2_atributos.png', 2, [((0,y),(445,180))\
                                                        for y in xrange(0, 540, 180)])
        self.button2_image = self.list_button2[0]
        self.button2_pos = (250, 300)

        self.list_button3 = load_image('carro3_atributos.png', 2, [((0,y),(445,180))\
                                                        for y in xrange(0, 540, 180)])
        self.button3_image = self.list_button3[0]
        self.button3_pos = (450, 500)

        self.advance_images = load_image('avancar.png', 2, [((0,y),(190,48))\
                                                for y in xrange(0, 144, 48)])
        self.advance_button = self.advance_images[0]
        self.advance_size = self.advance_button.get_size()
        self.advance_pos = (710, 720)
        
        self.a_car_size = self.button1_image.get_size()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.set_fullscreen()

            screen.blit(self.background, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            if self.button1_pos[0] <= mouse_pos[0] <= self.button1_pos[0] + self.a_car_size[0]\
            and self.button1_pos[1] <= mouse_pos[1] <= self.button1_pos[1] + self.a_car_size[1]:
                self.button1_image = self.list_button1[1]

                if mouse_press[0]:
                    self.button1_image = self.list_button1[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.car_selected = 1

            elif self.car_selected == 1:
                self.button1_image = self.list_button1[1]
            else:
                self.button1_image = self.list_button1[0]


            if self.button2_pos[0] <= mouse_pos[0] <= self.button2_pos[0] + self.a_car_size[0]\
            and self.button2_pos[1] <= mouse_pos[1] <= self.button2_pos[1] + self.a_car_size[1]:
                self.button2_image = self.list_button2[1]

                if mouse_press[0]:
                    self.button2_image = self.list_button2[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.car_selected = 2

            elif self.car_selected == 2:
                self.button2_image = self.list_button2[1]
            else:
                self.button2_image = self.list_button2[0]


            if self.button3_pos[0] <= mouse_pos[0] <= self.button3_pos[0] + self.a_car_size[0]\
            and self.button3_pos[1] <= mouse_pos[1] <= self.button3_pos[1] + self.a_car_size[1]:
                self.button3_image = self.list_button3[1]

                if mouse_press[0]:
                    self.button3_image = self.list_button3[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.car_selected = 3

            elif self.car_selected == 3:
                self.button3_image = self.list_button3[1]
            else:
                self.button3_image = self.list_button3[0]


            if self.back_pos[0] <= mouse_pos[0] <= self.back_pos[0] + self.back_size[0]\
            and self.back_pos[1] <= mouse_pos[1] <= self.back_pos[1] + self.back_size[1]:
                self.back_button = self.back_buttons[1]

                if mouse_press[0]:
                    self.back_button = self.back_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.back_button = self.back_buttons[1]
                    return

            else: self.back_button = self.back_buttons[0]

            if self.advance_pos[0] <= mouse_pos[0] <= self.advance_pos[0] + self.advance_size[0]\
            and self.advance_pos[1] <= mouse_pos[1] <= self.advance_pos[1] + self.advance_size[1]:
                self.advance_button = self.advance_images[1]

                if mouse_press[0]:
                    self.advance_button = self.advance_images[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.advance_button = self.advance_images[1]
                    if self.car_selected is not None:
                        self.select_level_menu()

            else: self.advance_button = self.advance_images[0]


            if not mouse_press[0]:
                self.pressed = False


            screen.blit(self.button1_image, self.button1_pos)
            screen.blit(self.button2_image, self.button2_pos)
            screen.blit(self.button3_image, self.button3_pos)
            screen.blit(self.back_button, self.back_pos)
            screen.blit(self.advance_button, self.advance_pos)
            screen.blit(self.text, (0, 0))

            pygame.display.flip()

            
    def select_level_menu(self):
        self.background = load_image('menu_background_2.bmp')
        self.text = load_image('sel_nivel.bmp', 2)
        
        levels = load_image('niveis.png', 2, [((0,y),(240,98))\
                                                            for y in xrange(0, 882, 98)])

        level_map = {'easy': 0, 'medium': 3, 'hard': 6}

        easy_image = levels[level_map['easy']]
        easy_pos = (392, 130)

        medium_image = levels[level_map['medium']]
        medium_pos = (391, 330)

        hard_image = levels[level_map['hard']]
        hard_pos = (392, 530)

        self.play_images = load_image('jogar.png', 2, [((0,y),(175,65))\
                                                for y in xrange(0, 195, 65)])
        self.play_button = self.advance_images[0]
        self.play_size = self.advance_button.get_size()
        self.play_pos = (710, 700)

        self.level_selected = None
        self.pressed = False


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.set_fullscreen()

            screen.blit(self.background, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            if easy_pos[0] <= mouse_pos[0] <= easy_pos[0] + 240\
            and easy_pos[1] <= mouse_pos[1] <= easy_pos[1] + 98:
                easy_image = levels[level_map['easy'] + 1]

                if mouse_press[0]:
                    easy_image = levels[level_map['easy'] + 2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.level_selected = 1

            elif self.level_selected == 1:
                easy_image = levels[level_map['easy'] + 1]
            else:
                easy_image = levels[level_map['easy']]


            if medium_pos[0] <= mouse_pos[0] <= medium_pos[0] + 240\
            and medium_pos[1] <= mouse_pos[1] <= medium_pos[1] + 98:
                medium_image = levels[level_map['medium'] + 1]

                if mouse_press[0]:
                    medium_image = levels[level_map['medium'] + 2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.level_selected = 2

            elif self.level_selected == 2:
                medium_image = levels[level_map['medium'] + 1]
            else:
                medium_image = levels[level_map['medium']]

            if hard_pos[0] <= mouse_pos[0] <= hard_pos[0] + 240\
            and hard_pos[1] <= mouse_pos[1] <= hard_pos[1] + 98:
                hard_image = levels[level_map['hard'] + 1]

                if mouse_press[0]:
                    hard_image = levels[level_map['hard'] + 2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.level_selected = 3

            elif self.level_selected == 3:
                hard_image = levels[level_map['hard'] + 1]
            else:
                hard_image = levels[level_map['hard']]
                

            if self.back_pos[0] <= mouse_pos[0] <= self.back_pos[0] + self.back_size[0]\
            and self.back_pos[1] <= mouse_pos[1] <= self.back_pos[1] + self.back_size[1]:
                self.back_button = self.back_buttons[1]

                if mouse_press[0]:
                    self.back_button = self.back_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.back_button = self.back_buttons[1]
                    return

            else: self.back_button = self.back_buttons[0]

            if self.play_pos[0] <= mouse_pos[0] <= self.play_pos[0] + self.play_size[0]\
            and self.play_pos[1] <= mouse_pos[1] <= self.play_pos[1] + self.play_size[1]:
                self.play_button = self.play_images[1]

                if mouse_press[0]:
                    self.play_button = self.play_images[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.play_button = self.play_images[1]
                    if self.level_selected is not None:
                        pygame.mixer.music.stop()
                        if main(screen, self.car_selected, self.level_selected) == False:
                            self.main_menu()

            else: self.play_button = self.play_images[0]


            if not mouse_press[0]:
                self.pressed = False


            screen.blit(easy_image, easy_pos)
            screen.blit(medium_image, medium_pos)
            screen.blit(hard_image, hard_pos)
            screen.blit(self.back_button, self.back_pos)
            screen.blit(self.play_button, self.play_pos)
            screen.blit(self.text, (0, 0))

            pygame.display.flip()


pygame.init()

screen = pygame.display.set_mode((pygame.display.Info().current_w,
                                  pygame.display.Info().current_h),
                                  pygame.FULLSCREEN)

pygame.display.set_caption("Test Drive")
menu = Menu()

if __name__ == "__main__":
    menu.main_menu()
