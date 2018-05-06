
import pygame
from pygame.locals import *
from sys import exit
import os
from math import *
import time
from functions import *
from loader import load_image

class Chronometer:

    def __init__(self):
        self.seconds = 0.0
        self.font = pygame.font.SysFont("arial", 18)
        self.font.set_bold(True)
        self.font_height = self.font.get_linesize()
        self.stop = True
        self.started_now = False

    def start(self, seconds):
        self.seconds = seconds
        self.stop = False
        self.started_now = True

    def set_time(self):
        if self.started_now:
            self.time = time.time()

    def run(self):
        self.started_now = False
        if self.seconds > 0.:
            if self.stop == False:
                new_time = time.time()
                self.seconds -= new_time - self.time
                self.time = new_time

        else:
            self.seconds = 0.0

    def show(self):
        text = 'Tempo: %1.2f' % self.seconds
        #write_in_screen(text, (255, 255, 255), 20, (10, 10))

class Semaforo:

    def __init__(self, seconds):
        'self.images = load_image2(semaforo.png, 2, [((x, 0), (94, 140)) \
                                                     for x in xrange(0, 188, 94)])'
        self.image = load_image('semaforo.png')
        self.rect = self.image.get_rect()
        #self.image = self.images[0]
        self.pos = (400, 380)
        self.screen = pygame.display.get_surface()
        self.chron = Chronometer()
        self.chron.start(seconds + 1.5)
        self.chron.set_time()
        self.finished = False
        self.opened = False
        print seconds

    def abre_semaforo(self):
        self.chron.run()
        if self.chron.seconds < 2.5:
            self.opened = True
            #self.image = self.images
        if self.chron.seconds == 0.0:
            self.finished = True

    def show(self):
        if not self.finished:
            self.screen.blit(self.image, self.pos)