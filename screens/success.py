# coding=utf-8
import pygame

from elements.label import Label
from elements.button import Button
from elements.image import Image
from elements.progress import Progress

from .screen import Screen

class SuccessScreen(Screen):
    def __init__(self, screen, **kwargs):
        super(SuccessScreen, self).__init__(screen)

        self.objects.append(Label(
            self.screen,
            text='Erfolgeich erfasst',
            pos=(30, 120),
            size=70
        ))

        self.objects.append(Button(
            self.screen,
            text='OK',
            pos=(50, 500),
            size=50,
            click=self.btn_home
        ))

        self.progress = Progress(
            self.screen,
            pos=(300, 600),
            size=100,
            on_elapsed=self.time_elapsed
        )
        self.objects.append(self.progress)
        self.progress.start()

    def time_elapsed(self):
        self.home()

    def home(self):
        from .screen_manager import ScreenManager
        screen_manager = ScreenManager.get_instance()
        screen_manager.set_default()

    def btn_home(self, param, pos):
        self.home()
